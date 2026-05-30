# 🎯 Corporate Asset Engine: Branded vCard Generator

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Pillow](https://img.shields.io/badge/Pillow-Image_Processing-brightgreen.svg)
![qrcode](https://img.shields.io/badge/qrcode-Data_Matrix-orange.svg)

A production-ready Python engine designed to generate highly customized, aesthetically stylized QR codes for B2B marketing and corporate networking. 

Unlike standard URL-based QR codes, this engine compiles a native **vCard 3.0** payload. When scanned, it bypasses the browser and directly triggers the native "New Contact" OS interface on iOS and Android devices, instantly porting corporate details (Organization, Email, Website, Phone) into the user's phone.

## 📐 System Architecture

The matrix generation pipeline utilizes high error-correction algorithms to intentionally sacrifice raw data capacity in exchange for structural redundancy, allowing for physical pixel occlusion (Logo Injection) without degrading scanner readability.

```mermaid
graph TD
    %% Define Nodes
    Payload[fa:fa-address-card vCard 3.0 Payload]
    Engine((fa:fa-cogs QR Engine))
    Styles[fa:fa-paint-brush Aesthetic Modifiers]
    Matrix[fa:fa-qrcode RGB Data Matrix]
    Logo[fa:fa-image Corporate Logo]
    Pillow{fa:fa-crop Pillow Image Processing}
    Output[fa:fa-download Final Corporate Asset]

    %% Define Flow
    Payload -->|Data Intake| Engine
    Styles -->|Rounded Dots & Hex Colors| Engine
    Engine -->|ERROR_CORRECT_H| Matrix
    Logo -->|Resizing & Calculation| Pillow
    Matrix --> Pillow
    Pillow -->|Center Coordinate Paste| Output

    %% Styling
    classDef primary fill:#2B6379,stroke:#0F0F0F,stroke-width:2px,color:#fff;
    classDef secondary fill:#459CCB,stroke:#0F0F0F,stroke-width:2px,color:#fff;
    class Payload,Logo,Styles secondary;
    class Engine,Matrix,Pillow,Output primary;
