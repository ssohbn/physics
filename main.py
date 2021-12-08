from decimal import *
getcontext().prec = 7
G = Decimal(9.81)


def momentum_PM(momentum, mass):
  momentum = Decimal(momentum)
  mass= Decimal(mass)
  velocity = momentum / mass 
  return velocity


def momentum_MV(mass, velocity):
  mass = Decimal(mass)
  velocity = Velocity(mass)

  momentum = mass * velocity
  return momentum

def momentum_PV(momentum, velocity):
  momentum = Decimal(momentum)
  velocity = Decimal(velocity)
  mass = momentum / velocity
  return mass


def inelastic_getFinal(mass1, velocity1, mass2, velocity2):
  mass1 = Decimal(mass1)
  velocity1= Decimal(velocity1)
  mass2 = Decimal(mass2)
  velocity2= Decimal(velocity2)

  finalVelocity = (mass1*velocity1 + mass2*velocity2)/(mass1+mass2)
  return finalVelocity

def inelastic_findv1(m1, m2, v2, vf):
  m1 = Decimal(m1)
  m2 = Decimal(m2)
  v2 = Decimal(v2)
  vf = Decimal(vf)
  v1 = ((m1 + m2)*vf - (m2*v2))/m1
  return v1

def elastic_gf1(m1, vi1, m2, vi2, vf2):
  m1 = Decimal(m1)
  m2 = Decimal(m2)
  vi2 = Decimal(vi2)
  vf2 = Decimal(vf2)

  momentum1 =m1*vi1 
  momentum2 = m2* vi2
  momentumf2 = m2 * vf2
  print(momentum1, momentum2, momentumf2)
  print(momentum1+momentum2-momentumf2)
  vf1 = ( momentum1+momentum2-momentumf2 )/Decimal(vf2)
  return vf1

def potentialEnergy(m,g,h):
  m = Decimal(m)
  g = Decimal(g)
  h = Decimal(h)
  pe = m*g*h
  return pe

def kineticEnergy(m, v):
  m = Decimal(m)
  v = Decimal(v)
  vv = v*v
  ke = Decimal(1/2) * m * vv
  return ke

def velocityPE(m, h):
  m = Decimal(m)
  h = Decimal(h)
  pe = potentialEnergy(m, G, h)
  v = ((2*pe)/m).sqrt()

  return v

print(f"""
{velocityPE(8, 45)}
""")
