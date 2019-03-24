import sendgrid

client = sendgrid.SendGridClient("SENDGRID_APIKEY")
message = sendgrid.Mail()

message.add_to("test@sendgrid.com")
message.set_from("you@youremail.com")
message.set_subject("Tu Titulo")
message.set_html("Tu mensaje")

client.send(message)
