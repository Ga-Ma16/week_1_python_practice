# Week 1: YouTube Analytics Dashboard

This project analyzes the top 1,000 most subscribed YouTube channels, utilizing a defensive data pipeline to clean the dataset and rendering the output into a custom, dark-mode HTML mega-dashboard. 

## System Architecture

```mermaid
graph TD
    A[Raw CSV Dataset] --> B[Data Engine: Pandas]
    B -->|Data Scrubbing & Formatting| C[Visualization Engine: Plotly]
    C -->|Generate Interactive Charts| D[UI Compiler: HTML/CSS]
    D -->|Export| E((dashboard.html))
    
    style A fill:#2D3748,stroke:#66FCF1,stroke-width:2px,color:#fff
    style B fill:#2D3748,stroke:#66FCF1,stroke-width:2px,color:#fff
    style C fill:#2D3748,stroke:#66FCF1,stroke-width:2px,color:#fff
    style D fill:#2D3748,stroke:#66FCF1,stroke-width:2px,color:#fff
    style E fill:#45A29E,stroke:#fff,stroke-width:2px,color:#fff
```
