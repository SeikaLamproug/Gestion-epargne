from django.core.mail.backends.smtp import EmailBackend
import ssl

class SSLEmailBackend(EmailBackend):
    def open(self):
        super().open()  # Établir la connexion en utilisant la méthode open de la classe parente
        if self.connection:  # Vérifier que la connexion a bien été établie
            try:
                self.connection.starttls(context=ssl.create_default_context(ssl.Purpose.CLIENT_AUTH, check_hostname=False))
            except ssl.SSLError:
                if not self.fail_silently:
                    raise