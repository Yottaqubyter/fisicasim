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

    def __init__(self,x,y,z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return "vector("+self.x+","+self.y+")"
    
    def __str__(self):
        return str(self.x)+"*(i)" + " + " + str(self.y)+"*(j)" + " + " + str(self.z)+"*(k)"
    
    def __eq__(self,other):
        return (self.x==other.x and self.y==other.y and self.z==other.z)

    def __add__(self, other):
        return vector(self.x+other.x,self.y+other.y,self.z+other.z)
    def __sub__(self, other):
        return vector(self.x-other.x,self.y-other.y,self.z-other.z)
    def __mul__(self, other):
        if type(other)==vector:
            return NotImplemented # Se podria implementar producto escalar
        else:
            return vector(self.x*other,self.y*other,self.z*other)
    def __matmul__(self, other):
        return NotImplemented # Se podria implementar producto cruz
    def __truediv__(self, other):
        return self*(1/other)
    def __floordiv__(self, other):
        if type(other)==vector:
            return NotImplemented
        else:
            return vector(self.x//other,self.y//other,self.z//other)
    def __mod__(self, other):
        return NotImplemented # Podria hacerse, pero inutil
    def __divmod__(self, other):
        return NotImplemented
    def __pow__(self, other):
        return NotImplemented
    def __lshift__(self, other):
        return NotImplemented
    def __rshift__(self, other):
        return NotImplemented
    def __and__(self, other):
        return NotImplemented
    def __xor__(self, other):
        return NotImplemented
    def __or__(self, other):
        return NotImplemented

    def __radd__(self, other): # other+self
        return vector(self.x+other.x,self.y+other.y,self.z+other.z)
    def __rsub__(self, other): # other-self
        return vector(other.x-self.x,other.y-self.y,other.z-self.z)
    def __rmul__(self, other): # other*self
        if type(other)==vector:
            return NotImplemented # Se puede añadir producto escalar
        else:
            return vector(self.x*other,self.y*other,self.z*other)
    def __rmatmul__(self, other):
        return NotImplemented # Se puede añadir producto cruz
    def __rtruediv__(self, other): # other/self(vecto) !!! No se puede dividir entre un vector
        return NotImplemented
    def __rfloordiv__(self, other):
        return NotImplemented
    def __rmod__(self, other):
        return NotImplemented
    def __rdivmod__(self, other):
        return NotImplemented
    def __rpow__(self, other):
        return NotImplemented
    def __rlshift__(self, other):
        return NotImplemented
    def __rrshift__(self, other):
        return NotImplemented
    def __rand__(self, other):
        return NotImplemented
    def __rxor__(self, other):
        return NotImplemented
    def __ror__(self, other):
        return NotImplemented

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self
    def __imul__(self, other):
        if type(other)==vector:
            return NotImplemented
        else:
            self.x *= other
            self.y *= other
            self.z *= other
            return self
    def __imatmul__(self, other):
        return NotImplemented
    def __itruediv__(self, other):
        self *= 1/other
        return self
    def __ifloordiv__(self, other):
        if type(other)==vector:
            return NotImplemented
        else:
            self.x //= other
            self.y //= other
            self.z //= other
            return self 
    def __imod__(self, other):
        return NotImplemented
    def __ipow__(self, other):
        return NotImplemented
    def __ilshift__(self, other):
        return NotImplemented
    def __irshift__(self, other):
        return NotImplemented
    def __iand__(self, other):
        return NotImplemented
    def __ixor__(self, other):
        return NotImplemented
    def __ior__(self, other):
        return NotImplemented
    
    def __neg__(self):
        return vector(-self.x,-self.y,-self.z)
    def __pos__(self):
        return vector(+self.x,+self.y,+self.z)
    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __int__(self):
        return vector(int(self.x),int(self.y),int(self.z))
    def __float__(self):
        return vector(float(self.x),float(self.y),float(self.z))

# Algunos vectores estandar
null_vector = vector(0,0)
i_vector = vector(1,0)
j_vector = vector(0,1)


class body:
# Por hacer: Modificar la clase para que solo se encargue de calculos matematicos (La parte de piglet la hago yo)
#            (Así no hay que modificar tantas cosas para crear AstralBodies3D)
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

if __name__=='__main__':
    print(2*i_vector)