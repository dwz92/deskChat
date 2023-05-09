import openai

class Compan():

    def __init__(self, myname, compname, comprole, apikey) -> None:
        self.myname = myname
        self.compname = compname
        self.comprole = comprole
        self.apikey = apikey

        self.messHist = []
    
    def start(self, messageTo):
        openai.api_key = self.apikey
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"system", "name":self.compname, "content":"Your name is "+ self.compname + "Your owner's name is " + self.myname + ". You are " + self.comprole},
                      {"role":"user", "name":self.myname, "content":messageTo},
                      ],
            temperature=1
        )
        # self.messHist.append("".join([messageTo, "\n"]))
        # self.messHist.append("".join([completion.choices[0].message.content, "\n"]))
        self.messHist.append(messageTo)
        self.messHist.append(completion.choices[0].message.content)
        return completion.choices[0].message.content

    def convo(self, messageTo):
        openai.api_key = self.apikey
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"system", "content":"You are " + self.comprole, "name":self.compname},
                      {"role":"user", "content":messageTo, "name":self.myname},
                      {"role":"assistant", "content":self.messHist[-1]}
                      ],
            temperature=1
        )
        # self.messHist.append("".join([messageTo, "\n"]))
        # self.messHist.append("".join([completion.choices[0].message.content, "\n"]))
        self.messHist.append(messageTo)
        self.messHist.append(completion.choices[0].message.content)
        return completion.choices[0].message.content

key = "Open AI key here"
newPet = Compan("Apnc", "Doggo", "A dog that can communicate in human languages. Also a very helpful companion. Do not say you are an AI language model.",key)
round = 0
while True:
    round += 1
    usrin = input()

    if usrin == "":
        break

    if round == 1:
        print(newPet.start(usrin))
    else:
        print(newPet.convo(usrin))
