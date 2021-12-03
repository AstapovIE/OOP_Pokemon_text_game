class Team:
    def __init__(self, name, masters=None, doctors=None, spectators=None, PokemonForFight=None, MasterForFight=None, DoctorForFight=None):
        self.name = name
        if masters == None:
            masters = []
        self.masters = masters
        if doctors == None:
            doctors = []
        self.doctors = doctors
        if spectators == None:
            spectators = []
        self.spectators = spectators
        self.PokemonForFight = PokemonForFight
        self.MasterForFight = MasterForFight
        self.DoctorForFight = DoctorForFight

    def chose_master(self, Master, pokemon):
        # if MasterForFight in self.masters:
        Master.chose_pokemon(pokemon, self)
        self.MasterForFight = Master
        # else:
        # raise ValueError('такого мастера нет в этой команде')

    def chose_doctor(self, Doctor):
        self.DoctorForFight = Doctor

    def info(self):
        print('тима состоит из : ')
        if type(self.masters) == list:
            for master in self.masters:
                master.info()
        else:
            self.masters.info()
        if type(self.doctors) == list:
            for doctor in self.doctors:
                doctor.info()
        else:
            self.doctors.info()
        if type(self.spectators) == list:
            for spectator in self.spectators:
                spectator.info()
        else:
            self.spectators.info()
        if self.PokemonForFight == None:
            print('покемон не выбран')
        else:
            self.PokemonForFight.info()
