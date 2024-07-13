def GetTextUser(message):
    text=""
    typeMessage= message["type"]
    
    if  typeMessage=="text":
        text=(message["text"])["body"]
    elif typeMessage == "interactive":
        interactiveObject = message["interactive"]
        typeInteractive = interactiveObject["type"]
        if typeInteractive == "button_reply":
            text=(interactiveObject["button_reply"])["title"]
        elif typeInteractive=="list_reply":
            text=(interactiveObject["list_reply"])["title"]
        else:
            print("sin mensaje")
    else:
        print("sin mensaje")
    
    return text


def TextMessage(text, number):
    data = {
        "messaging_product": "whatsapp",    
        "to": number,
        "type": "text",
        "text": {
            "body": text
        }
    }
    return data

def ImageMessage(number):
    data = {
        "messaging_product": "whatsapp",    
        "to": number,
        "type": "image",
        "image": {
            "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/image_whatsapp.png"
        }
    }
    return data

def DocumentMessage(number):
    data = {
        "messaging_product": "whatsapp",    
        "to": number,
        "type": "document",
        "document": {
            "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/document_whatsapp.pdf"
        }
    }
    return data

def LocationMessage(number):
    data = {
    "messaging_product": "whatsapp",
    "to": number,
    "type":"location",
    "location": {
        "latitude":"41.5553413444904",
        "longitude":"2.0910084386686436",
        "name":"Estadi Nova Creu Alta",
        "address":"Plaça d'Olímpia, 1, 08206 Sabadell, Barcelona"
    }
}
    return data


def ButtonsMessage(number):
    data = {
    "messaging_product": "whatsapp",
    "to": number,
    "type": "interactive",
    "interactive": {
        "type": "button",
        "body": {
            "text": "¿Confirmas tu aceptación?"
        },
        "action": {
            "buttons": [
                {
                    "type": "reply",
                    "reply": {
                        "id": "001",
                        "title": "✅Si"
                    }
                },
                {
                    "type": "reply",
                    "reply": {
                        "id": "002",
                        "title": "❌No"
                    }
                }
            ]
        }
    }
}
    return data


def ListMessage(number):
    data = {
    "messaging_product": "whatsapp",
    "to": number,
    "type": "interactive",
    "interactive": {
        "type": "list",
        "body": {
            "text": "✅ I have these options"
        },
        "footer": {
            "text": "Select an option"
        },
        "action": {
            "button": "See options",
            "sections": [
                {
                    "title": "Buy and sell products",
                    "rows": [
                        {
                            "id": "main-buy",
                            "title": "Buy",
                            "description": "Buy the best product your home"
                        },
                        {
                            "id": "main-sell",
                            "title": "Sell",
                            "description": "Sell your products"
                        }
                    ]
                },
                {
                    "title": "📍center of attention",
                    "rows": [
                        {
                            "id": "main-agency",
                            "title": "Agency",
                            "description": "Your can visit our agency"
                        },
                        {
                            "id": "main-contact",
                            "title": "Contact center",
                            "description": "One of our agents will assist you"
                        }
                    ]
                }
            ]
        }
    }
}
    return data

