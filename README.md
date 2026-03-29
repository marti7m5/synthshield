## 🚀 SynthShield

Synthetic Data Defense for Security & Surveillance AI

SynthShield is a synthetic data pipeline designed for privacy-safe computer vision training.

It generates realistic synthetic scenes, automatically applies bounding box annotations, and produces training-ready datasets without relying on sensitive real-world imagery.

Built in 24 hours at RevolutionUC.

---

## 🖥️ Live Demo

👉 https://synthshield.tech

Generate synthetic scenes and view:
- Raw procedurally generated environments  
- Automatically labeled outputs  
- YOLO-style training-ready data  

---

## 🧠 Problem

Modern AI systems in security, surveillance, and healthcare require large amounts of labeled data. Using real-world data introduces:

- Privacy risks  
- Regulatory challenges  
- Data exposure vulnerabilities  

---

## 💡 Solution

SynthShield replaces sensitive datasets with realistic synthetic data generated in controlled environments.

The system produces:
- Synthetic scenes  
- Automatic YOLO-style annotations  
- Visual validation of labeled outputs  

This enables safe development, testing, and validation of AI systems.

---

## 🔬 Pipeline

1. **Scene Generation (Blender)**
   - Randomized object placement  
   - Variable object counts per scene  

2. **Automatic Annotation**
   - YOLO-format bounding boxes  
   - Generated directly from scene data  

3. **Visualization**
   - Side-by-side raw vs labeled output  
   - Interactive web demo  

---

## 🔥 Features

- Privacy-preserving dataset generation  
- Fully automated labeling pipeline  
- Randomized synthetic environments  
- Interactive demo with real outputs  
- Scalable to large training datasets  

---

## 🧩 Use Cases

- Surveillance system training without real footage  
- Healthcare AI without patient data exposure  
- Defense and security simulation environments  
- Synthetic datasets for research and testing  

---

## 🛠️ Tech Stack

- **Blender** → synthetic scene generation  
- **Python** → data pipeline + annotation generation  
- **HTML/CSS/JS** → interactive frontend demo  
- **GitHub Pages** → deployment  

---

## 🚀 Future Work

- Accurate 3D → 2D bounding box projection  
- Lighting, occlusion, and environment variation  
- Domain-specific datasets (healthcare, traffic, defense)  
- Integration with model training pipelines  

---

## 👤 Author

**Michael Martina**  
Cybersecurity @ University of Cincinnati  

---

## 📁 Project Structure
synthshield/
├── README.md
├── index.html
├── scanner.py
├── datagen/
│ ├── generate.py
│ ├── annotations/
│ │ └── .gitkeep
│ ├── images/
│ │ └── .gitkeep
│ └── masks/
│ └── .gitkeep
