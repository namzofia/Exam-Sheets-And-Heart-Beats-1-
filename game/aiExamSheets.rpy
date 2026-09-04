init python:
    import json
    import urllib.request
    import urllib.parse
    import ssl
    import pygame.scrap
    import pygame.constants

    # API Configuration
    GEMINI_API_KEY = "AQ.Ab8RN6Li7kd-qmzofJXD8-9EFoBGPFXp2Nw88Fw6g7nvtoTZCQ"
    ssl_context = ssl._create_unverified_context()

    # Clipboard Helpers
    def get_clipboard_text():
        """Fetches text directly from the OS clipboard."""
        try:
            pygame.scrap.init()
            text = pygame.scrap.get(pygame.SCRAP_TEXT)
            if text:
                return text.decode('utf-8').replace('\x00', '').strip()
        except Exception:
            pass
        return ""

    def paste_clipboard_to_answer():
        """Button action that appends clipboard text to the player's answer."""
        global player_answer
        pasted = get_clipboard_text()
        if pasted:
            player_answer = player_answer + pasted
        renpy.restart_interaction()

    def paste_clipboard_to_notes():
        """Button action that sets clipboard text to study notes."""
        global persistent_study_notes
        pasted = get_clipboard_text()
        if pasted:
            persistent_study_notes = pasted
        renpy.restart_interaction()

    # Escapes Ren'Py's text-tag characters so AI output never breaks dialogue/screen text
    def sanitize_ai_text(text):
        if not text:
            return text
        return text.replace("[", "[[").replace("{", "{{")

    # Gemini API Functions
    def generate_ai_question(study_text):
        clean_key = urllib.parse.quote(GEMINI_API_KEY.strip())
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key={clean_key}"
        
        notes_content = str(study_text)[:2000] if study_text else "Photosynthesis in plants."
        
        prompt = (
            "You are an exam generator. Read the following study notes and generate ONE short test question. "
            "Output ONLY the question text.\n\nNotes:\n" + notes_content
        )
        
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        headers = {'Content-Type': 'application/json'}
        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers)
        
        try:
            response = urllib.request.urlopen(req, context=ssl_context, timeout=15)
            result = json.loads(response.read().decode('utf-8'))
            question = result['candidates'][0]['content']['parts'][0]['text'].strip()
            return sanitize_ai_text(question)
        except Exception as e:
            return f"Error generating question: {str(e)}"

    def check_ai_answer(question, user_answer, study_text):
        clean_key = urllib.parse.quote(GEMINI_API_KEY.strip())
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key={clean_key}"
        
        notes_content = str(study_text)[:2000] if study_text else "Photosynthesis in plants."
        
        prompt = (
            f"Notes: {notes_content}\n"
            f"Question: {question}\n"
            f"Student Answer: {user_answer}\n\n"
            "Evaluate the student's answer using the notes.\n"
            "RULES FOR YOUR RESPONSE:\n"
            "1. If correct, start with: 'CORRECT!' followed by 1 brief sentence of praise.\n"
            "2. If incorrect, start with: 'INCORRECT! The correct answer was [insert answer], because [insert 1 brief sentence explanation]'."
        )
        
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        headers = {'Content-Type': 'application/json'}
        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers)
        
        try:
            response = urllib.request.urlopen(req, context=ssl_context, timeout=15)
            result = json.loads(response.read().decode('utf-8'))
            answer = result['candidates'][0]['content']['parts'][0]['text'].strip()
            return sanitize_ai_text(answer)
        except Exception as e:
            return f"Error checking answer: {str(e)}"

# Labels for Execution
label triggerAiAction:
    $ ai_question = generate_ai_question(persistent_study_notes)
    $ player_answer = ""
    show screen resultTestPopup
    pause

label evaluateActionAnswer:
    $ ai_result = check_ai_answer(ai_question, player_answer, persistent_study_notes)
    
    e "[ai_result]"

    if "CORRECT" in ai_result and "INCORRECT" not in ai_result:
        jump expression ("act" + selectedAction + "Pass")
    else:
        jump expression ("act" + selectedAction + "Fail")