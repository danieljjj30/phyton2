from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import logging

# Configuración básica
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Datos de tu emprendimiento (personaliza esto)
RESPUESTAS = {
    "bien": "Bien gracias 😊, Con que informacion puedo ayudarte sobre nosotros Sweet Spot",
    "productos": "🍰 Te ofrecemos unas ricas tortas por porciones y galletas 🍪:\n- Chocolate\n- Tres leches\n- Vainilla con cubierta y relleno de arequipe\n- Choco quesillo \n- Galletas polvorosas\n¡😊En que otra cosa puedo ayudarte!",
    "precios": "💰 Nuestros precios:\n 🍰Tortas \n- Chocolate 3$ \n- Tres leches 3$ \n- Vainilla con cubierta y relleno de arequipe 2.5$ \n- Choco quesillo 3.5$ \n- 🍪Galletas polvorosas 1.5$ al detal 1$ al mayor a partir de 6 unidades\n¡😊En que otra cosa puedo ayudarte!",
    "envios": "🚚 Envíos a toda cabimas:\n\n• Costo: Dependiendo de la zona\n• Envio gratis por compras mayores a 10$\n¡😊En que otra cosa puedo ayudarte! ",
    "contacto": "📞 Contáctanos:\n\nWhatsApp: 0412-1422179\nInstagram: @Sweetspot_29\n 😊Necesitas ayuda en algo mas!",
    "pagos": "💳 Aceptamos:\n\n• Efectivo\n• Transferencia\n• Pago movil\n 😊Tienes alguna otra inquietud",
    "Pedidos de tortas completas": "🍰 Tortas de 1KG :\n- Chocolate 33$ \n- Tres leches 33$ \n- Vainilla con cubierta y relleno de arequipe 27$ \n- Choco quesillo 39$ \n\n 🍰 Tortas de 1/2KG \n- Chocolate 16$ \n- Tres leches 16$ \n- Vainilla con cubierta y relleno de arequipe 15$ \n- Choco quesillo 20$ \n\n🍰 Tortas de 1/4KG :\n- Chocolate 39$ \n- Tres leches 9$ \n- Vainilla con cubierta y relleno de arequipe 8$ \n- Choco quesillo 11$ \n\n¡😊Para realizar pedidos contactanos",
    "devoluciones": "🔄no se aceptan devoluciones"
}

# Comando /start personalizado
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Holaaa {user.first_name} 😊\n\n"
        "✨ *Bienvenido/a a mi pequeño emprendimiento Sweep Spot!* ✨\n\n"
        "Tú apoyo lo hace grande 💕\n\n"
        "¿En qué podemos ayudarte hoy? Puedes preguntarme sobre:\n"
        "- Productos disponibles\n- Precios\n- Envíos\n- Contacto\n- Ubicación\n"
        "- O cualquier otra inquietud que tengas\n\n"
        "¡Estoy aquí para ayudarte! 💌",
        parse_mode='Markdown'
    )
# Manejador de mensajes
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    
    if any(palabra in text for palabra in ['hola', 'hi', 'buenos días']):
        await update.message.reply_text(f"¡Hola {update.effective_user.first_name}! ¿Cómo estás?")
    
    elif any(palabra in text for palabra in ['bien', 'y tu', 'gracias']):
        await update.message.reply_text(RESPUESTAS["bien"])

    elif any(palabra in text for palabra in ['producto', 'productos', 'servicio']):
        await update.message.reply_text(RESPUESTAS["productos"])

    elif any(palabra in text for palabra in ['precio', 'costó', 'valor', 'cuánto sale', 'precios', 'cuanto vale', 'que precios tienen los productos', 'en que precios salen los productos']):
        await update.message.reply_text(RESPUESTAS["precios"])
    
    elif any(palabra in text for palabra in ['envío', 'envios', 'entrega', 'cuándo llega']):
        await update.message.reply_text(RESPUESTAS["envios"])
    
    elif any(palabra in text for palabra in ['contacto', 'hablar', 'whatsapp', 'teléfono']):
        await update.message.reply_text(RESPUESTAS["contacto"])
    
    elif any(palabra in text for palabra in ['pago', 'pagos', 'tarjeta', 'pago movil','transferencia','transferencias']):
        await update.message.reply_text(RESPUESTAS["pagos"])
    
    elif any(palabra in text for palabra in ['devolución', 'devolver', 'cambio']):
        await update.message.reply_text(RESPUESTAS["devoluciones"])
    
    elif any(palabra in text for palabra in ['gracias', 'thanks']):
        await update.message.reply_text("¡De nada DIOS te bendiga! 😊 ¿Necesitas algo más?")
        
    elif any(palabra in text for palabra in ['torta', 'completa' , 'completas' , 'al mayor']):
        await update.message.reply_text(RESPUESTAS["Pedidos de tortas completas"])
    else:
        await update.message.reply_text(
            "No entendí tu pregunta relacionada con Sweet Spot . Puedes reformular tu pregunta o intentar con:\n"
            "- 'Quiero saber los precios'\n"
            "- '¿Cómo son los envíos?'\n"
            "- '¿Dónde los contacto?'"
        )

# Manejo de errores
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Error: {context.error}")
    if update.message:
        await update.message.reply_text("Ocurrió un error. Por favor intenta nuevamente.")

def main():
    # Configura tu token aquí
    application = Application.builder().token("7841638412:AAGso5OXD-tsQhRJxNPXH1LTHH66XzQ_S0g").build()
    
    # Manejadores
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Manejo de errores
    application.add_error_handler(error_handler)
    
    # Iniciar el bot
    logger.info("Bot iniciado. Presiona Ctrl+C para detenerlo.")
    application.run_polling()

if __name__ == '__main__':
    main()