import pyPLUTO as pypl
import pyPLUTO.pload as pp
import pyPLUTO.ploadparticles as pr
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import sys

perg = 9.38e8  # eV
# plutodir = os.environ['PLUTO_DIR']
# wdir = 'C:/Users/filte/Documents/PLUTO/YMSC_MSC_1/poisk_uv/'

# wdir = 'C:/Users/filte/Documents/PLUTO/Wd2_shell/out9/'
# wdir = 'C:/Users/filte/Documents/PLUTO/Termination/MF_n05_5_cont/'
wdir = 'C:/Users/filte/Documents/PLUTO/Termination/Cluster_2_48_2/'  #

# f = open('id1.dat', 'w')
# nlinf = pypl.nlast_info(w_dir=wdir, datatype='vtk')
# file1=np.loadtxt('exact.dat')
# file2=np.loadtxt('/home/alexandra/Documents/PLUTO/PLUTO/YMSC/particle.05.dat')


# D = pp.pload(nlinf['nlast'],w_dir=wdir,datatype='vtk')
# D = pp.pload(10,w_dir=wdir,datatype='vtk')
D = pp.pload(29, varNames=['prs', 'Bx1', 'Bx2', 'Bx3'], w_dir=wdir, datatype='vtk')

# N=500
# N1
bmod = np.sqrt(D.Bx1 ** 2 + D.Bx2 ** 2 + D.Bx3 ** 2)

# P = pr.ploadparticles(0,w_dir=wdir,datatype='dbl')
# gamma=np.sqrt(1+(P.vx1**2 + P.vx2**2+P.vx3**2)/(299.792458)**2)
# p_eng = np.sqrt(P.vx1**2 + P.vx2**2+P.vx3**2)/gamma

# for i in range (len(p_eng)):

#    f.write (str("{:6.0f}".format(P.id[i]))+'\n')
# print (perg*gamma)
# indx_sort = p_eng.argsort()
# indx_sort = P.x1.argsort()
# for i in range (50):
# print(P.x1[indx_sort[i]])
# x1s, x2s, pengs = P.x2[indx_sort], P.x3[indx_sort], perg*gamma[indx_sort]
# bxy=np.zeros((N, N))
# bxy[:,:]=bmod[1, :, :]
# bxy=bxy.T
# im0 = plt.imshow(bxy[:, :],extent=[D.x2.min(), D.x2.max(), D.x3.max(), D.x3.min()],norm=colors.LogNorm())
# plt.gca().invert_yaxis() # optional
# im1 = plt.scatter(x1s[1:500], x2s[1:500],s=10,c=pengs[1:500],cmap='inferno',alpha=0.7)
# print (x1s[1:20], x2s[1:20])
# plt.colorbar(im1, orientation='horizontal')
# plt.plot(D.x3, D.Bx1[:,1])
# plt.minorticks_on()

# sys.exit(1)


UVjump = 1.5
UVjumpHi = 10.5
log_jump = np.log(UVjump)
log_jump1 = np.log(UVjumpHi)


# UVarr=np.zeros((N, N))
# UV3D=np.zeros((N, N, N))

def funcnear(i, j, k):
    kol = 0
    if log_jump1 > (np.log(bmod[i][j][k] / bmod[i + 1][j][k])) > log_jump and log_jump1 > (
    np.log(D.prs[i][j][k] / D.prs[i + 1][j][k])) > log_jump:
        kol = 1  # kol+1
    if log_jump1 > (np.log(bmod[i][j][k] / bmod[i - 1][j][k])) > log_jump and log_jump1 > (
    np.log(D.prs[i][j][k] / D.prs[i - 1][j][k])) > log_jump:
        kol = 1  # kol+1
    if log_jump1 > (np.log(bmod[i][j][k] / bmod[i][j + 1][k])) > log_jump and log_jump1 > (
    np.log(D.prs[i][j][k] / D.prs[i][j + 1][k])) > log_jump:
        kol = 1  # kol+1
    if log_jump1 > (np.log(bmod[i][j][k] / bmod[i][j - 1][k])) > log_jump and log_jump1 > (
    np.log(D.prs[i][j][k] / D.prs[i][j - 1][k])) > log_jump:
        kol = 1  # kol+1
    if log_jump1 > (np.log(bmod[i][j][k] / bmod[i][j][k + 1])) > log_jump and log_jump1 > (
    np.log(D.prs[i][j][k] / D.prs[i][j][k + 1])) > log_jump:
        kol = 1  # kol+1
    if log_jump1 > (np.log(bmod[i][j][k] / bmod[i][j][k - 1])) > log_jump and log_jump1 > (
    np.log(D.prs[i][j][k] / D.prs[i][j][k - 1])) > log_jump:
        kol = 1  # kol+1

    return kol


kol2 = 0

f = open('uv_coords_48o_100k1.dat', 'w')
for k in range(100, 400, 2):
    print(k)
    for j in range(100, 400, 2):
        for i in range(100, 400, 2):
            # UV3D[i, j, k]=funcnear(i, j, k)
            # kol2=kol2+funcnear(i, j, k)
            if (funcnear(i, j, k) > 0):
                f.write(str("{:6.3f}  {:6.3f}  {:6.3f}".format(D.x1[i], D.x2[j], D.x3[k])) + '\n')
                # f.write (str("{:6d}  {:6d}  {:6d}".format(i, j, k))+'\n')
                # UVarr[j,k]=1
            # UVarr[j, k]=UVarr[j,k]+funcnear(i, j, k)
        # if (UVarr[j,k]>1):
        #	UVarr[j,k]=1

# print (kol2)
f.close()
# f = open('uv_coords.dat', 'r')
# f1=np.loadtxt('uv_coords.dat')
# fig, ax = plt.subplots()
# divider = make_axes_locatable(ax)
# cax = divider.append_axes('right', size='5%', pad=0.05)
# plt.imshow(bmod[150,:,:],extent=[D.x2.min(), D.x2.max(), D.x3.min(), D.x3.max()],norm=colors.LogNorm())
# im=plt.imshow(UVarr[:,:], cmap='Purples')#,extent=[0,1,0,1])#, norm=colors.LogNorm())
# im = plt.scatter(f1[:,2], f1[:,1],c=f1[:, 0])
# im = plt.scatter(f1[:,1], f1[:,2],c=f1[:, 0])
# im= ax.imshow(tr2_jk[:,:], extent=[0,1,0,1])
# plt.colorbar(im, orientation='vertical')
