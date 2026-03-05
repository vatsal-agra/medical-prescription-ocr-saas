# Medical Prescription OCR SaaS

A deployed SaaS tool that allows doctors to upload multiple patient prescriptions and automatically generates a consolidated clinical summary — saving time and reducing manual record review.

## What It Does

Doctors frequently need to review a patient's prescription history across multiple visits and providers. This tool streamlines that process:

1. **Upload** — doctor uploads multiple prescription documents (images or PDFs)
2. **OCR Extraction** — the system extracts text from each prescription using OCR
3. **LangChain Processing** — extracted text is processed through a LangChain pipeline that understands medical context
4. **Summary Generation** — an LLM generates a clean, structured clinical summary highlighting medications, dosages, patterns, and relevant history
5. **Output** — doctor receives a consolidated summary ready for clinical use

## Built As Part Of

This tool was developed as a standalone SaaS component of **InsuTrack**, a dual-portal healthcare platform connecting doctors and patients. The OCR SaaS handles the prescription history intelligence layer independently.

## Tech Stack

- **Python** — core processing
- **LangChain** — document processing pipeline and LLM orchestration
- **Streamlit** — web interface and deployment
- **OCR (Tesseract / Document AI)** — text extraction from prescription images and PDFs
- **LLM API** — clinical summary generation

## Key Concepts Demonstrated

- LangChain document processing pipelines
- OCR integration for real-world document handling
- Medical text processing and summarisation
- SaaS deployment with Streamlit
- Practical LLM application in healthcare

## How to Run

```bash
# Install dependencies
install the requirements.txt file into the same folder and they will download automatically when you run app.py
# Run the app
streamlit run app.py
```

## Use Case

- Doctors reviewing patients with complex medication histories
- Reducing time spent manually reading through multiple prescriptions
- Identifying medication overlaps or patterns across visits

---

**Note:** This project handles medical data. In a production environment, appropriate data privacy and compliance measures (HIPAA/DPDP) would need to be implemented.

---

**Author:** Vatsal Agrawal  
**GitHub:** [github.com/vatsal-agra](https://github.com/vatsal-agra)  
**LinkedIn:** [linkedin.com/in/vatsal-agrawal-a7a9641b0](https://linkedin.com/in/vatsal-agrawal-a7a9641b0)
