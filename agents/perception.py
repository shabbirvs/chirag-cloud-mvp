from PIL import Image
import io

def run_perception(preset: str, uploaded_file=None) -> dict:
    """
    Extracts raw visual or document features.
    Simulates edge-level perception / YOLO triage.
    """
    if uploaded_file is not None:
        filename = uploaded_file.name
        file_bytes = uploaded_file.getvalue()
        # Basic image dimension extraction if image
        try:
            img = Image.open(io.BytesIO(file_bytes))
            width, height = img.size
            format_type = img.format
        except Exception:
            width, height, format_type = 0, 0, "Document/PDF"
            
        detected_features = {
            "source": "User Upload",
            "filename": filename,
            "resolution": f"{width}x{height}",
            "type": format_type,
            "detected_objects": ["apparel_item", "drape_pattern"] if "Retail" in preset else ["clinical_notes", "emirates_id", "insurance_card"],
            "quality_score": 0.94
        }
    else:
        # Fallback to simulated preset features
        if "Retail" in preset:
            detected_features = {
                "source": "Sample Preset: Arabian Open Abaya",
                "garment_class": "Open Abaya with Embroidered Trim",
                "color_palette": ["Deep Charcoal", "Rose Gold Thread"],
                "lighting_check": "Optimal / Minimal Studio Background",
                "quality_score": 0.98
            }
        else:
            detected_features = {
                "source": "Sample Preset: Clinic Encounter Receipt",
                "extracted_fields": ["Patient ID: 784-XXXX-XXXXXXX-1", "Diagnosis: Acute Pharyngitis", "CPT: 99213"],
                "payer": "Daman Enhanced",
                "quality_score": 0.96
            }

    return detected_features