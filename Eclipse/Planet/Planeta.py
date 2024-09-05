from Planet.Moon import Moon

class Planeta: 

    def __init__(self, semiEixoUA, raioPlanJup, periodo, anguloInclinacao, ecc, anom, raioStar, mass, moon: Moon = ()): 
        self.lua = moon # NOTE: Lua opcional?
        self.semiEixoUA = semiEixoUA
        self.raioPlanJup = raioPlanJup
        self.periodo = periodo
        self.anguloInclinacao = anguloInclinacao
        self.ecc = ecc
        self.anom = anom 
        self.mass = mass * (1.898 *(10**27)) #passar para gramas por conta da constante G
        
        # Calculos
        self.semiEixoRaioStar = self.calcSemEixoRaioStar(raioStar)

        # NOTE:: semiEixoPixel = self.semiEixoRaioStar * self.raioEstrelaPixel #nao sei se vou precisar
        self.raioPlanetaRstar = self.calcRaioPlanetaRaioStar(raioStar)

    def calcSemEixoRaioStar(self, raioStar): 
        return ((1.469*(10**8))*self.semiEixoUA)/raioStar
    
    def calcRaioPlanetaRaioStar(self, raioStar): 
        return (self.raioPlanJup*69911)/raioStar # multiplicando pelo raio de jupiter em km 

    def getRaioPlanPixel(self, raioEstrelaPixel): 
        return self.raioPlanetaRstar * raioEstrelaPixel
    
    def getRaioPlan(self):
        return self.raioPlanetaRstar

    def getRplanJup(self):
        return self.raioPlanJup

    def getSemiEixo(self):
        return self.semiEixoUA
    
    def getsemiEixoRaioStar(self):
        return self.semiEixoRaioStar

    def getPeriodo(self):
        return self.periodo

    def getInc(self):
        return self.anguloInclinacao

    def getEccAnom(self):
        return self.ecc, self.anom 