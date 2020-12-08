# Esta libreria incluye algunas funciones, clases y variables, usadas en el proyecto


def opsum(l):
    k = l[0]
    for i in l[1:]:
        k += i
    return k

def istype(l, tp):
    for i in l:
        if type(i)!=tp:
            return False
    return True

class vector:

    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __repr__(self):
        return "vector("+self.x+","+self.y+")"
    
    def __str__(self):
        return (str(self.x)+"*(i)")*(self.x!=0) + (" + ")*(self.x!=0 and self.y!=0) + (str(self.y)+"*(j)")*(self.y!=0)
    
    def __eq__(self,other):
        return (self.x==other.x and self.y==other.y)
    
    def __add__(self,other):
        return vector(self.x+other.x,self.y+other.y)

    def __iadd__(self,other):
        self.x += other.x
        self.y += other.y
        return self
    
    def __sub__(self,other):
        return vector(self.x-other.x,self.y-other.y)
    
    def __mul__(self,other):
        if type(other)==vector:
            return NotImplemented
        else:
            return vector(self.x*other,self.y*other)
        
    def __truediv__(self,other):
        return self*(1/other)
    
    def __floordiv__(self,other):
        if type(other)==vector:
            return NotImplemented
        else:
            return vector(self.x//other,self.y//other)



    def __radd__(other,self):
        return vector(self.x+other.x,self.y+other.y)
    
    def __rsub__(other,self):
        return vector(self.x-other.x,self.y-other.y)
    
    def __rmul__(other,self):
        if type(other)==vector:
            return NotImplemented
        else:
            return vector(self.x*other,self.y*other)
        
    def __rtruediv__(other,self):
        return self*(1/other)
    
    def __rfloordiv__(other,self):
        if type(other)==vector:
            return NotImplemented
        else:
            return vector(self.x//other,self.y//other)


    def __neg__(self):
        return vector(-self.x,-self.y)

    def __pos__(self):
        return vector(+self.x,+self.y)

    def __abs__(self):
        return (self.x**2+self.y**2)**0.5

# Algunos vectores estandar
null_vector = vector(0,0)
i_vector = vector(1,0)
j_vector = vector(0,1)


class body:
    """
Clase baul para la creacion de clases específicas a cada simulación.
Clases hijo creadas:
    · astralBody
    """
    def __init__(self, pgbody, wdata, r0, *args):
        if not istype((r0,)+args , vector):
            raise TypeError("Expected vector type arguments: body(pyglet shape, vector, ...)")
        self.rva0 = [r0]+list(args) # [r, dr/dt, d**2r/dt**2, d**3r/dt**3]
        self.wdata = wdata
        pgbody.x = r0.x*3 + wdata.x/2
        pgbody.y = r0.y*3 + wdata.y/2
        self.pgbody = pgbody
    
    def update(self,dt):
        for i in range(self.get_n()-1):
            self.rva0[i] += self.get_dnr_dtn(i+1)*dt
        self.pgbody.x = self.rva0[0].x*3 + self.wdata.x/2
        self.pgbody.y = self.rva0[0].y*3 + self.wdata.y/2

    def get_n(self):
        return len(self.rva0)

    def get_dnr_dtn(self,n):
        return self.rva0[n]


class astralBody(body):
    """docstring for astralBody"""
    def __init__(self, pgbody, wdata, mass, bodySpace, r0=null_vector, v0=null_vector):
        super(astralBody, self).__init__(pgbody, wdata, r0, v0)
        self.mass = mass
        if not istype(bodySpace, astralBody):
            raise TypeError("Expected (astralBody,···,astralBody,) type argument")
        self.bodySpace = bodySpace

    def update(self,dt):
        super(astralBody,self).update(dt)

    def get_n(self):
        return 3

    def get_dnr_dtn(self,n):
        try:
            return super(astralBody,self).get_dnr_dtn(n)
        except IndexError as e:
            if n>3:
                raise e
            return opsum([
                (atractor.get_dnr_dtn(0)-self.get_dnr_dtn(0))*atractor.mass*0.01
                /
                abs(atractor.get_dnr_dtn(0)-self.get_dnr_dtn(0))**3 
                for atractor in filter(lambda x:x!=self and x!=None, self.bodySpace)])
