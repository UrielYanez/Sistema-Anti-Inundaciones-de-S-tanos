# 🚨 Sistema Anti-Inundaciones de Sótanos ⚡  
**Autores:** Uriel Yañez Aguayo y Jose Armando Ruano Mascorro  
*Proyecto final de la materia Aplicaciones de IoT*

## Diagrama del Sistema


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
# 📋 Especificaciones Técnicas Detalladas
## 🔌 Hardware
| Componente               | Especificaciones Técnicas               | Ubicación en el Sistema       |
|--------------------------|-----------------------------------------|--------------------------------|
| ESP32                    | WiFi 802.11 b/g/n, Bluetooth 4.2        | Unidad central de control      |
| Sensor de Agua           | Voltaje: 3.3V, Salida Analógica         | Nivel del piso                 |
| HC-SR04 (Ultrasónico)    | Rango: 2-400cm, Precisión: 3mm          | Techo del sótano               |
| Bomba de Agua            | 5V DC, 5L/min,                          | Punto más bajo del sótano      |
| Tira LED RGB WS2812B     | 10 LED's                                | Zona de alerta visual          |

## 📊 Dashboard en Node-RED
![Imagen de WhatsApp 2025-04-24 a las 13 39 39_191269a1](https://github.com/user-attachments/assets/3b5d07aa-7c9c-40af-a93c-8fbcec5c53c1)



## ⚡ Diagrama de Conexiones
Agregar diagrama
