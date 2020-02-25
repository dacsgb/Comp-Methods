import numpy as np

class Node():
    def __init__(self):
        self.name = None
        self.x = None
        self.y = None

class Link():
    def __init__(self):
        self.name = None
        self.node1name = None
        self.node2name = None
        self.node1 = None
        self.node2 = None
        self.length = None
        self.angle = None

class Support():
    def __init__(self):
        self.name = None
        self.node = None
        self.direction = None

class Force():
    def __init__(self):
        self.name = None
        self.node = None
        self.Fx = None
        self.Fy = None

class Truss():
    def __init__(self):
        self.title = None
        self.d_units = None
        self.f_units = None
        self.Sut = None
        self.Sy = None
        self.E = None
        self.nStatic = None
        self.nFatigue = None
        self.nBuckling = None
        self.d_min = None

        self.nodes = []
        self.links = []
        self.support = []
        self.forces = []
        self.loadsets = []

        self.longest = -np.inf
        self.shortest = np.inf
        self.shortestLink = None
        self.longestLink = None

        self.averageLength = 0

    def Read(self,data):
        for line in data:

            cells = line.strip().split(',')

            keyword = cells[0].lower()
            
            if keyword == 'title': self.title = cells[1].replace("'","")

            if keyword == 'distance_unit': self.d_units = cells[1].strip()

            if keyword == 'force_unit': self.f_units = cells[1].strip()

            if keyword == 'material':
                            self.Sut = float(cells[1])
                            self.Sy = float(cells[2])
                            self.E = float(cells[3])

            if keyword == 'fatigue_factor': self.nFatigue = float(cells[1].strip())
            
            if keyword == 'static_factor': self.nStatic = float(cells[1].strip())

            if keyword == 'buckling_factor': self.nBuckling = float(cells[1].strip())

            if keyword == 'min_diameter': self.d_min = float(cells[1].strip())

            if keyword == 'node':
                holder = Node()
                holder.name = cells[1].strip()
                holder.x = float(cells[2].strip())
                holder.y = float(cells[3].strip())
                self.nodes.append(holder)
            
            if keyword == 'link':
                holder = Link()
                holder.name = cells[1].strip() 
                holder.node1name = cells[2].strip()
                holder.node2name = cells[3].strip()
                self.links.append(holder)
            
            if keyword == 'support':
                holder = Support()
                holder.name = cells[1].strip()
                holder.node = cells[2].strip()
                holder.direction = cells[3].strip()
                self.support.append(holder)
            
            if keyword == 'force':
                holder = Force()
                holder.name = cells[1].strip()
                holder.node = cells[2].strip()
                holder.Fx = float(cells[3].strip())
                holder.Fy = float(cells[4].strip())
                self.forces.append(holder)

        self.Update()
    
    def Update(self):
        for link in self.links:
            for node in self.nodes:
                if node.name == link.node1name:
                    link.node1 = node
                if node.name == link.node2name:
                    link.node2 = node
        
        cumulative = 0

        for link in self.links:
            x1 = link.node1.x
            y1 = link.node1.y
            x2 = link.node2.x
            y2 = link.node2.y

            dx = x2 - x1
            dy = y2 - y1

            link.length = np.hypot( dx , dy)
            link.angle = np.arctan2(dy , dx)

            cumulative += link.length

            if link.length > self.longest:
                self.longest = link.length
                self.longestLink = link

            if link.length < self.shortest:
                self.shortest = link.length
                self.shortestLink = link
        
        self.averageLength = cumulative/len(self.links)

    def Report(self):
        rpt = '\t \t Truss Design Report \n \n \n'

        rpt += ' ***************** Title *****************' + '\n'

        rpt += str(self.title)+ '\n'

        rpt+= '\n'

        rpt += ' ***************** Units *****************' + '\n'

        if self.d_units != None: rpt += 'Distance Units:' + '\t' + '\t' + str(self.d_units) + '\n' 

        if self.f_units != None: rpt += 'Force Units:' + '\t' + '\t' + str(self.f_units) + '\n'

        rpt += 'Angle Units: \t \t rad \n'

        rpt += '\n'

        rpt += ' ***************** Factors of Safety *****************' + '\n'

        if self.nFatigue != None: rpt += 'Fatigue Factor of Safety:' + '\t' + str(self.nFatigue) + '\n'

        if self.nStatic != None: rpt += 'Static Factor of Safety:' + '\t' + str(self.nStatic) + '\n'

        if self.nBuckling != None: rpt += 'Buckling Factor of Safety' + '\t' +str(self.nBuckling) + '\n'

        rpt += '\n'

        rpt += ' ***************** Minimum Dimensions *****************'+ '\n'

        if self.d_min != None: rpt += 'Minimum Diameter:' + '\t' +str(self.d_min) + '\n'

        rpt += '\n'

        rpt += ' ***************** Material Properties *****************' + '\n'

        if self.Sut != None: rpt += 'Ultimate Strength:' + '\t' + str(self.Sut) +'\n'

        if self.Sy != None: rpt += 'Yeild Strength:' + '\t' + '\t' + str(self.Sy) +'\n'

        if self.E != None: rpt += 'Modulus of Elasticity:' + '\t' + str(self.E) +'\n'

        rpt += '\n'

        rpt += ' ***************** Link Summary *****************' + '\n'

        rpt += 'Link \t (1) \t (2) \t Length \t Angle \n'

        for link in self.links:
            rpt += str(link.name) +'\t'+str(link.node1.name) +'\t'+ str(link.node2.name)+'\t {:.2f} \t {:.2f}'.format(link.length,link.angle) + '\n'
            
        return rpt
