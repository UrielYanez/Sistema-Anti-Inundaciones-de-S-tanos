# 🚨 Sistema Anti-Inundaciones de Sótanos   
**Autores:** Uriel Yañez Aguayo y Jose Armando Ruano Mascorro  
*Proyecto final de la materia Aplicaciones de IoT*

---

## 🌟 Características Clave
- 🚿 Detección en tiempo real de niveles de agua
- 🌡️ Monitoreo ambiental (temperatura/humedad)
- 🚨 Sistema de alertas mediante email
- 💧 Activación automática de bomba de agua
- 📊 Registro histórico en base de datos

---

## 🛠️ Arquitectura del Sistema
```mermaid
graph TD
    A[Sensores] --> B{ESP32}
    B --> C[Raspberry Pi]
    C --> D[(PostgreSQL)]
    C --> E[Node-RED Dashboard]
    B --> F[Actuadores]
    F --> G[Bomba de Agua]
    F --> H[Buzzer]
    F --> I[Leds]
```

---
# 📋 Especificaciones Técnicas Detalladas
## 🔌 Hardware
| Componente               | Especificaciones Técnicas               | Ubicación en el Sistema       |
|--------------------------|-----------------------------------------|--------------------------------|
| ESP32                    | WiFi 802.11 b/g/n, Bluetooth 4.2        | Unidad central de control      |
| Sensor de Agua           | Voltaje: 3.3V, Salida Analógica         | Nivel del piso                 |
| HC-SR04 (Ultrasónico)    | Rango: 2-400cm, Precisión: 3mm          | Techo del sótano               |
| Bomba de Agua            | 5V DC, 5L/min,                          | Punto más bajo del sótano      |
| Tira LED RGB WS2812B     | 10 LED's                                | Zona de alerta visual          |
| Buzzer                   | Voltaje: 5V, Frecuencia: 2-4kHz         | Zona de alerta auditiva        |
| Driver L298N             | Voltaje: 5V                             | Control de bomba de agua       |
| DHT11                    | Rango: 20-80% HR, 0-50°C, Salida digital| Área central del sóbano        |


## 📊 Dashboard en Node-RED
![Imagen de WhatsApp 2025-04-24 a las 13 39 39_191269a1](https://github.com/user-attachments/assets/3b5d07aa-7c9c-40af-a93c-8fbcec5c53c1)

---

## ⚡ Diagrama de Conexiones
![Imagen de WhatsApp 2025-04-24 a las 13 50 42_2a27503a](https://github.com/user-attachments/assets/773b3dce-f372-4b82-82df-9fd67702721d)

---

## 🔧 Desarrollo del Prototipo
<img src="https://github.com/user-attachments/assets/253db2f9-d4c9-4d9f-977e-02b377714a09" style="width:30%; display: inline-block;" alt="Prototipo 1">
<img src="https://github.com/user-attachments/assets/4c15d0a2-40b0-4569-8aa1-dca9b373511a" style="width:30%; display: inline-block;" alt="Prototipo 2">
<img src="https://github.com/user-attachments/assets/2f17ecfe-b21e-4254-847e-92a124317c08" style="width:30%; display: inline-block;" alt="Prototipo 3">

---

## ⚡ Validación del Proyecto


---

## 🏆 Resultados Obtenidos

