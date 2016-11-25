
from nanohttp import settings

from restfulpy.messaging.messenger import Messenger
from restfulpy.configuration import configure


class ConsoleMessenger(Messenger):
    def send_from(self, from_, to, subject, body, cc=None, bcc=None, template_string=None, template_filename=None):
        """
        Sending messages by email
        """

        body = self.render_body(body, template_string, template_filename)
        print(body)


if __name__ == '__main__':
    configure()
    settings.merge("""
    smtp:
      host: smtp.gmail.com
      port: 587
      username: *******@gmail.com
      password: **********
      local_hostname: example.com
    """)

    template = """
    <ul>
        <li>Hi</li>
        <li>token: ${token}</li>
    </ul>
    """

    broker = ConsoleMessenger()
    broker.send(
        "vahid@carrene.com",
        "Test", {
            'token': '%^ERFV%^RV%^RFV$DV$%DV54dc4d54d54d4d%$D$D$'
        },
        template_string=template
    )