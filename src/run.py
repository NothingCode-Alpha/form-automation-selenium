import automation
import form_inputs
from time import sleep
name = form_inputs.name_input
email =  form_inputs.email_input
message = form_inputs.message_input
bot = automation.FormAutomation()
bot.form_link("http://127.0.0.1:5500/form.html")
bot.informations()
bot.form_filler(name , email , message)
sleep(5)
bot.submit()
sleep(5)
bot.quit()