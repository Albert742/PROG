 ```mermaid
graph LR
    A[Internet] --> B(Firewall)
    B --> C{TOR}
    C --> D(Main Server)
    D --> E((FS))
    D --> F((ERP))
    D --> G((AC))
    D --> H((DC))
    B --> I(Workstations)
    style E fill:#f9f,stroke:#333,stroke-width:2px
    style F fill:#f9f,stroke:#333,stroke-width:2px
    style G fill:#f9f,stroke:#333,stroke-width:2px
    style H fill:#f9f,stroke:#333,stroke-width:2px
    subgraph Small Company Network
    I
    D
    end
```