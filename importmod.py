import datetime

class MessageUser():
    user_details=[]
    message=[]
    base_message="""hii {name}!
Thank you for the purchase on {date}.
i hope you are excited about using it.
Just as a reminder the purchase total was ${total}.

"""
    
    def add_user(self,name,amount):
        name=name[0].upper()+name[1:].lower()
        amount="%2f"%(amount)
        detail={
                 "name":name,
                 "amount":amount,
        }
        today=datetime.date.today()
        date_text='{today.day}/{today.month}/{today.year}'.format(today=today)
        detail["date"]=date_text
        self.user_details.append(detail)

    def get_detail(self):
        return self.user_details
    def make_messsages(self):
        if len(self.user_details) > 0:
              for detail in self.get_detail():
                  name = detail["name"]
                  date = detail["date"]
                  amount = detail["amount"]
                  message = self.base_message
                  new_message = message.format(
                      name=name,
                      date=date,
                      total=amount
                      )
                  self.message.append(new_message)
              return self.message
        return []



obj=MessageUser()
obj.add_user("priyanka",152.0)
obj.add_user("priyal",113.44)
obj.add_user("pravin",156.9)
obj.add_user("pradnya",159.8)
obj.get_detail()

def random():
    print("hiiiii")
    









            
