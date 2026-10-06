import os
import streamlit as st
from groq import Groq

def run_strategy(extracted_features: dict, preset: str) -> str:
    """
    Applies reasoning, business context, or billing logic via Groq LLM.
    """
    # Safely retrieve key from st.secrets or environment variable
    api_key = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY"))
    
    if not api_key:
        return f"[Simulated Output - Missing GROQ_API_KEY in Secrets]: Processed features for {preset} successfully."

    client = Groq(api_key=api_key)

    if "Retail" in preset:
        system_prompt = (
            "You are the CHIRAG Strategy Agent for retail boutique marketing. "
            "Generate an engaging Instagram/WhatsApp portfolio post including: "
            "1. Catchy headline, 2. Garment styling notes, 3. Call to action, 4. Local trending hashtags."
        )
    else:
        system_prompt = (
            "You are the CHIRAG Strategy Agent for UAE Healthcare RCM. "
            "Evaluate extracted patient/billing features. Suggest applicable ICD-10 and CPT codes, "
            "flag prior-authorization needs, and format an HL7/FHIR validation summary."
        )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Input features: {extracted_features}"}
        ],
        temperature=0.2,
        max_tokens=600
    )

    return response.choices[0].message.content