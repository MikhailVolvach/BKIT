class MusOrch:
    """
    'Музыканты оркестра' для реализации связи многие-ко-многим
    """
    def __init__(self, orch_id, mus_id):
        self.mus_id = mus_id
        self.orch_id = orch_id

