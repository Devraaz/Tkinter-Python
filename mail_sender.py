import customtkinter as ctk
import tkinter as tk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter.messagebox as msg





def send_mail():
    mail_address = email_input.get()
    text_message = message_input.get("1.0", tk.END)


    message = MIMEMultipart()
    message["From"] = "Devraj Dora"
    message["To"] = mail_address
    message.attach(MIMEText(text_message, "plain"))

    sender_address = "contact.webokraft@gmail.com"
    sender_password = "vwbh akkj lfmx roye"


    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_address, sender_password )

        server.sendmail(sender_address, mail_address, message.as_string())
        server.quit()

        email_input.delete(0, tk.END)
        message_input.delete("1.0", tk.END)
        msg.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        msg.showerror("Error", f"Failed to send email:\n{e}")
        
    pass

root = ctk.CTk()
root.geometry("400x500")
root.title("Send Mail")

heading = ctk.CTkLabel(root, text="Email Sending", font=("", 20, "bold")).pack()
# -------------------------
# -------Frame  1----------
# -------------------------
frm1 = ctk.CTkFrame(root, corner_radius=10)
frm1.pack(ipadx = 10, ipady = 10, fill = "x", padx=10, pady = 10)
# khnb jiex qwqu tjpk

email_lb = ctk.CTkLabel(frm1, text = "Email: ").grid(row=0, column=0)
message_lb = ctk.CTkLabel(frm1, text = "Message: ").grid(row=1, column=0, ipadx=10, sticky="w")

email_input = ctk.CTkEntry(frm1, width=200)
email_input.grid(row=0, column = 1, sticky = "w", pady = 10)
message_input = ctk.CTkTextbox(frm1,width=200, height=100)
message_input.grid(row=1, column = 1, ipady=10)

send_btn = ctk.CTkButton(frm1, text="Send", command=send_mail)
send_btn.grid(row=2, column=1, pady=10)

root.mainloop()
