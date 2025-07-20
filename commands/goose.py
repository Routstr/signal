from signalbot import Command, Context
import subprocess
import re

import os

system_prompt = """
When I say proxy, I'm referring to the repository Routstr/proxy, when I say chat app or chat.routstr.com, I'm referring to the repo Routstr/routstr-chat, when I say sixty nuts, Routstr/sixty-nuts, when I say the main frontend or routstr.com, i'm referring to Routstr/frontend and when I say scripts, I'm referring to Routstr/scripts. Proxy is our backend server, chat app is our AI chat interface, frontend is our landing page and sixty nuts is a python package we've built to interact with Cashu, a bitcoin lightning payments protocol.

We do project management using github projects and project number 1 in there. We track issues of all projects using that.

Creating issues. When I ask you to create issues, you should always create using the github-pro tool, add that issue to project 1 and update the label to todo label, fetch labels if you have to. You'd always be sending a message about it to a signal recipient.

When we ask you to make changes to github, you should be using the tool github-pro to create pull requests and editing files. 
"""

class GooseCommand(Command):
    def describe(self) -> str:
        return "Honk! Honk! You called the goose!"

    async def handle(self, c: Context):
        command = c.message.text
        groups = c.bot.groups
        recipient = c.message.source_uuid
        if c.message.is_group():
            for group_data in groups:
                if group_data.get('internal_id') == c.message.group:
                    recipient = group_data.get('id')
                    break

        
        if any(greeting in command.lower() for greeting in ["hey goose", "hello goose", "hi goose"]):
            # result = subprocess.run(["goose", "run", "--no-session", "-t", "Fetch all the issues from Routstr/proxy, Routstr/routstr-chat and Routstr/frontend and summarize it under the heading **Summary of Current Issues** using the tool 'github-pro'. Each repository should get a brief summarize of the current issues. No need to display issues. Show no more than 3 main points per respository and send that output to the recipient "+ group_id + " be sure to format your message in markdown. "], capture_output=True, text=True)
            # result = subprocess.run(["goose", "run", "--no-session", "-t", command+". Here's your signal recipient: "+ group_id + " Be sure to style the message using ** for bold, ` for monospace and * for italics ", "--system", system_prompt], capture_output=True, text=True)
            result = subprocess.run(["pwd"], capture_output=True, text=True)
            pwd = result.stdout.strip()
            # result = subprocess.run(["goose", "run", "--no-session", "--recipe", "./routstr_management.yaml", "--params", "task=\"" + command+". Here's your signal recipient: "+ group_id + "   Be sure to style the message using ** for bold, ` for monospace and * for italics \""], capture_output=True)
            print("got the qeury, "+ command)
            result = subprocess.run(["goose", "run", "--no-session", "--recipe", "./routstr_management.yaml", "--params", "task=" + command+". Here's your signal recipient: " + recipient + " Be sure to style the signal message using **bold text** for bold, `code` for monospace and *text* for italics and use numbers when needed. ", "--params", "path=" + pwd, "--debug"], capture_output=True, text=True)
            ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
            cleaned_output = ansi_escape.sub('', result.stdout)
            print(f"Goose command output (cleaned): {cleaned_output}")
            return