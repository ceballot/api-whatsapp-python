from flask import Flask, request
import util
import whatsappservice
import chatgptservice

app = Flask(__name__)

@app.route('/welcome', methods=['GET'])
def index():
    return "Welcome developer"

@app.route('/whatsapp', methods=['GET'])
def VerifyToken():

    try:
        accessToken="SHA1234567890KKKLLL"
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token!= None and challenge != None and token == accessToken:
            return challenge
        else:
            return "", 400
    except:
        return "", 400
    

@app.route('/whatsapp', methods=['POST'])
def ReceivedMessage():
    
    try:
        body=request.get_json()
        entry = (body["entry"])[0]
        changes = (entry["changes"])[0]
        value = changes["value"] 
        message = (value["messages"])[0]   
        number = message["from"]    
        
        text=util.GetTextUser(message)

        responseGPT = chatgptservice.GetResponse(text)
        if responseGPT != "error":
            data = util.TextMessage(responseGPT, number)
        else:
            data = util.TextMessage("Lo siento, ocurrió un problema", number)
        whatsappservice.SendMessageWhatsapp(data)

        # ProcessMessage(text,number)

        return "EVENT_RECEIVED"
    except:
        return "EVENT_RECEIVED"


def ProcessMessage(text, number):
    text=text.lower()
    listData = []
    
    if "hola" in text:
        data = util.TextMessage("Hola, ¿en qué puedo ayudarte?", number)
        listData.append(data)
        dataMenu = util.ListMessage(number)
        listData.append(dataMenu)

    elif "gracias" in text:
        data = util.TextMessage("Gracias por contactar", number)
    elif "agency" in text:
        data = util.TextMessage("Esta es nuestra agencia", number)
        listData.append(data)
        dataLocation = util.LocationMessage(number)
        listData.append(dataLocation)
    elif "contact" in text:
        data = util.TextMessage("*Contact center:*\n00385467", number)
        listData.append(data)
    elif "buy" in text:
        data = util.ButtonsMessage(number)
        listData.append(data)
    elif "sell" in text:
        data = util.ButtonsMessage(number)
        listData.append(data)
    else:
        data = util.TextMessage("Lo siento, no puedo entenderte", number)
        listData.append(data)
        dataMenu = util.ListMessage(number)
        listData.append(dataMenu)

    for item in listData:
        whatsappservice.SendMessageWhatsapp(item)

def GenerateMessage(text,number):
       
    text=text.lower()
        
    if "text" in text:
        data = util.TextMessage("Text", number)
    if "image" in text:
        data = util.ImageMessage(number)
    if "document" in text:
        data = util.DocumentMessage(number)
    if "location" in text:
        data = util.LocationMessage(number)
    if "button" in text:
        data = util.ButtonsMessage(number)
    if "list" in text:
        data = util.ListMessage(number)
    
    whatsappservice.SendMessageWhatsapp(data)





if(__name__=="__main__"):
    app.run()