import numpy as np
import math

def radToDeg(radians):
    return radians * (180/np.pi)

def degToRad(degrees):
    return degrees * (np.pi/180)

def rotX(phi):
    Rx = [[1,0,0],
          [0, math.cos(phi), math.sin(phi)],
          [0, (-1) * math.sin(phi), math.cos(phi)]]
    return Rx

def rotY(theta):
    Ry = [[math.cos(theta),0,(-1) * math.sin(theta)],
          [0, 1, 0],
          [math.sin(theta), 0, math.cos(theta)]]
    return Ry

def rotZ(psi):
    Rz = [[math.cos(psi),math.sin(psi),0],
          [(-1) * math.sin(psi), math.cos(psi), 0],
          [0, 0, 1]]
    return Rz

def rotMatrix_xyz(phi, theta, psi):
    Rx = rotX(phi)
    Ry = rotY(theta)
    Rz = rotZ(psi)
    xyzRot = np.matmul(Rx, np.matmul(Ry,Rz))
    return xyzRot

def rotMatrix_zxz(phi, theta, psi):
    Rz = rotZ(phi)
    Rx = rotX(theta)
    Rz2 = rotZ(psi)
    zxzRot = np.matmul(Rz, np.matmul(Rx,Rz2))
    return zxzRot

## get XYZ values from rotation matrix (we will give zxz here as input)
def eulerXYZ(rotMat):
    phi = np.arctan2(rotMat[1][2], rotMat[2][2])
    theta = -np.arcsin(rotMat[0][2])
    psi = np.arctan2(rotMat[0][1], rotMat[0][0])
    return (phi,theta,psi)

## get ZXZ values from rotation matrix (we will give xyz here as input)
def eulerZXZ(rotMat):
    phi = np.arctan2(rotMat[0][2], rotMat[1][2])
    theta = np.arccos(rotMat[2][2])
    psi = np.arctan2(rotMat[2][0], -rotMat[2][1])
    return (phi, theta, psi)

## testing out the values
phiDeg_xyz = 30
thetaDeg_xyz = 45
psiDeg_xyz = -45

print("Euler angles XYZ [{}, {}, {}]".format(phiDeg_xyz, thetaDeg_xyz, psiDeg_xyz))

phiRad_xyz = degToRad(phiDeg_xyz)
thetaRad_xyz = degToRad(thetaDeg_xyz)
psiRad_xyz = degToRad(psiDeg_xyz)

Rxyz = rotMatrix_xyz(phiRad_xyz, thetaRad_xyz, psiRad_xyz)
phiRad_zxz, thetaRad_zxz, psiRad_zxz = eulerZXZ(Rxyz)
phiDeg_zxz = radToDeg(phiRad_zxz)
thetaDeg_zxz = radToDeg(thetaRad_zxz)
psiDeg_zxz = radToDeg(psiRad_zxz)
print("Euler angles ZYZ [{}, {}, {}]".format(phiDeg_zxz, thetaDeg_zxz, psiDeg_zxz))

Rzxz = rotMatrix_zxz(phiRad_zxz, thetaRad_zxz, psiRad_zxz)
phiRad_xyz_new, thetaRad_xyz_new, psiRad_xyz_new = eulerXYZ(Rzxz)

phiDeg_xyz_new = radToDeg(phiRad_xyz_new)
thetaDeg_xyz_new = radToDeg(thetaRad_xyz_new)
psiDeg_xyz_new = radToDeg(psiRad_xyz_new)
print("Euler angles XYZ_new [{}, {}, {}]".format(phiDeg_xyz_new, thetaDeg_xyz_new, psiDeg_xyz_new))

## XYZ and XYZ_new euler angles are same. So the conversion is correct
