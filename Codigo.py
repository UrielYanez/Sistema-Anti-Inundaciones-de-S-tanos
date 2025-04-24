from umqtt.simple import MQTTClient
from machine import Pin, ADC, PWM
from hcsr04 import HCSR04;
from time import sleep
import neopixel
import network
import umail
import dht

# -----Conexión a Internet-----
def conectar_wifi():
    print("Conectando...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Armando', 'Hola1234')
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.3)
    print("WiFi Conectada!")
    
def conecta_broker():
    client = MQTTClient(MQTT_CLIENT_ID,
    MQTT_BROKER, port=MQTT_PORT,
    user=MQTT_USER,
    password=MQTT_PASSWORD,
    keepalive=60)
    client.connect()
    print("Conectado a %s, en el topico %s"%(MQTT_BROKER, MQTT_TOPIC))
    return client

conectar_wifi()


# -----Conexión al Tópico-----
MQTT_BROKER = "192.168.137.166"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC = "AU/Proyecto"
MQTT_PORT = 1883

client = conecta_broker()


# -----Configuración Email-----
smtp_host       = "smtp.gmail.com"
smtp_port       = 465
sender_email    = "ruanoarmando54@gmail.com"
sender_password = "lklo xskf cgwh tkhj"
recipient_email = "aguayomar77@gmail.com"

def send_email(subject, body_text):
    mail = umail.SMTP(
        host=smtp_host,
        port=smtp_port,
        username=sender_email,
        password=sender_password,
        ssl=True
    )
    mail.to(recipient_email)

    mail.write("From: {}\r\n".format(sender_email))
    mail.write("To: {}\r\n".format(recipient_email))
    mail.write("Subject: {}\r\n".format(subject))
    mail.write("MIME-Version: 1.0\r\n")
    mail.write("Content-Type: text/html; charset=UTF-8\r\n")
    mail.write("\r\n")
    html = """\
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8">
    <title>{subj}</title>
  </head>
  <body style="font-family:Arial,sans-serif; background:#f4f4f4; margin:0; padding:20px;">
    <table width="100%%" cellpadding="0" cellspacing="0" border="0">
      <tr>
        <td align="center">
          <table width="600" cellpadding="0" cellspacing="0" border="0" style="background:#ffffff; border-radius:8px; overflow:hidden; box-shadow:0 2px 8px rgba(0,0,0,0.1);">
            <!-- Header -->
            <tr>
              <td style="background:#004aad; color:#ffffff; padding:20px; text-align:center; font-size:24px;">
                Alerta de Bomba de Agua
              </td>
            </tr>
            <!-- Body -->
            <tr>
              <td style="padding:30px; color:#333333; line-height:1.5;">
                <p>Hola,</p>
                <p>Se ha detectado un cambio en el estado de la <strong>bomba de agua</strong>:</p>
                <p style="font-size:18px; color:#004aad; margin:20px 0;"><em>{body}</em></p>
                <p>Puedes revisar el sistema para más detalles.</p>
                <p>Saludos,<br>
                   <strong>Equipo de Monitoreo AU</strong></p>
              </td>
            </tr>
            <!-- Footer -->
            <tr>
              <td style="background:#f4f4f4; padding:15px; text-align:center; font-size:12px; color:#777777;">
                © 2025 AU Monitoreo · <a href="https://google.com" style="color:#004aad; text-decoration:none;">Visita nuestro sitio</a>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </body>
</html>
""".format(subj=subject, body=body_text.replace("\n", "<br>"))

    mail.write(html)
    mail.send()
    mail.quit()

    print("Email enviado:", subject)


# -----Configuración de Sensores-----
sensor_HCSR04 = HCSR04(trigger_pin = 16, echo_pin = 17, echo_timeout_us = 24000);
sensor_agua = ADC(Pin(33))
sensor_agua.atten(ADC.ATTN_11DB)
sensor_DHT11 = dht.DHT11(Pin(4))
UMBRAL_AGUA = 1000

# -----Configuración de tira LED
NUM_LEDS = 10
PIN_LED = 15
np = neopixel.NeoPixel(Pin(PIN_LED), NUM_LEDS)

def actualizar_tira_led(distancia):
    if distancia >= 15:
        leds_encendidos = 0
    elif distancia <= 0:
        leds_encendidos = NUM_LEDS
    else:
        leds_encendidos = int((15 - distancia) / 1.5)

    for i in range(NUM_LEDS):
        if i < leds_encendidos:
            np[i] = (0, 0, 255)
        else:
            np[i] = (0, 0, 0)

    np.write()


# -----Configuración de el buzzer -----
buzzer = PWM(Pin(19))

def sonido():
    buzzer.freq(1000)
    buzzer.duty(512)
    sleep(1)
    buzzer.duty(0)
    
# -----Configuración de la Bomba de Agua-----
in1 = Pin(5, Pin.OUT)
in2 = Pin(18, Pin.OUT)

def activarBomba():
    in1.on()
    in2.off()

def apagarBomba():
    in1.off()
    in2.off()
    
estadoAnterior = ""

# -----Configuración de automatización de la bomba-----
while True:
    #sensor_DHT11.measure()
    #temp = sensor_DHT11.temperature()  # Temperatura en °C
    #hum = sensor_DHT11.humidity()  # Humedad en %
    distancia = sensor_HCSR04.distance_cm();
    valor = sensor_agua.read()
    
    print(f"Distancia: {distancia} cm")    
    print("------------------")
    
    actualizar_tira_led(distancia)
        
    if valor > UMBRAL_AGUA or distancia < 10:
        activarBomba()
        sonido()
        estadoBomba = "Activada"
        estadoActual = "¡¡¡Agua detectada, EL SOTANO SE ESTA INUNDANDO!!!\nTodo se va a ir alv\nAcciones preventivas: \n"
        print("Valor del sensor: ", valor, estadoActual)
    else:
        estadoActual = "Ningun problema, el sotano NO se esta inundando :)"
        estadoBomba = "Apagada"
        print("Valor del sensor: ", valor, estadoActual)
        apagarBomba()
        client = conecta_broker()
    
    if valor > 1000:
        agua = "Detectada"
    else:
        agua = "No hay"
    
    if estadoActual != estadoAnterior:
        estadoAnterior = estadoActual
        mensaje = f"Estado bomba: {estadoBomba}, Estado de agua: {agua}, Distancia al agua: {distancia} cm."
        client.publish(MQTT_TOPIC, f"{mensaje}")
        body = f"""
        <p><strong>Estado:</strong> {estadoActual}</p>
        <ul>
          <li>Estado de la bomba: {estadoBomba}</li>
          <li>Sensor de agua: {agua}</li>
          <li>Distancia al agua: {distancia} cm</li>
        </ul>
        """
        send_email("Alerta de la bomba", body)
    sleep(2)