from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from plot_B import plot_B
from plot_B_1d import plot_B_1d
from plot_B_1d_series import plot_B_1d_series
from plot_B_animated import plot_B_animated
from plot_B_animated_1d import plot_B_animated_1d
from plot_B_animated_window import plot_B_animated_window
from plot_B_quiver import plot_B_quiver
from plot_B_quiver_animated import plot_B_quiver_animated
from plot_B_window import plot_B_window
from plot_Bx import plot_Bx
from plot_Bx_window import plot_Bx_window
from plot_By import plot_By
from plot_By_window import plot_By_window
from plot_Bz import plot_Bz
from plot_Bz_window import plot_Bz_window

from plot_density import plot_density
from plot_density_1d_window import plot_density_1d_window
from plot_density_animated import plot_density_animated
from plot_density_1d import plot_density_1d
from plot_density_1d_series import plot_density_1d_series
from plot_density_animated_window import plot_density_animated_window
from plot_density_window import plot_density_window
from plot_density_animated_1d import plot_density_animated_1d

from plot_distribution import plot_distribution
from plot_distribution_animated import plot_distribution_animated
from plot_energy import plot_energy
from plot_escaped_distribution import plot_escaped_distribution

from plot_gamma import plot_gamma
from plot_gamma_1d import plot_gamma_1d
from plot_gamma_1d_series import plot_gamma_1d_series
from plot_gamma_animated import plot_gamma_animated
from plot_gamma_animated_1d import plot_gamma_animated_1d
from plot_gamma_animated_window import plot_gamma_animated_window
from plot_gamma_rtheta import plot_gamma_rtheta
from plot_gamma_rtheta_animated import plot_gamma_rtheta_animated
from plot_gamma_window import plot_gamma_window

from plot_particles import plot_particles
from plot_particle_trajectory import plot_particle_trajectory
from plot_particles_animated import plot_particles_animated
from plot_particles_animated_cyl import plot_particles_animated_cyl

from plot_pressure import plot_pressure
from plot_pressure_1d import plot_pressure_1d
from plot_pressure_1d_series import plot_pressure_1d_series
from plot_pressure_animated import plot_pressure_animated
from plot_pressure_animated_1d import plot_pressure_animated_1d
from plot_pressure_animated_window import plot_pressure_animated_window
from plot_pressure_window import plot_pressure_window
from plot_shock_wave import plot_shock_wave

from plot_temperature import plot_temperature
from plot_temperature_1d import plot_temperature_1d
from plot_temperature_1d_series import plot_temperature_1d_series
from plot_temperature_animated import plot_temperature_animated
from plot_temperature_animated_1d import plot_temperature_animated_1d
from plot_temperature_animated_window import plot_temperature_animated_window
from plot_temperature_window import plot_temperature_window

from plot_velocity import plot_velocity
from plot_velocity_1d import plot_velocity_1d
from plot_velocity_1d_series import plot_velocity_1d_series
from plot_velocity_1d_window import plot_velocity_1d_window
from plot_velocity_animated import plot_velocity_animated
from plot_velocity_animated_1d import plot_velocity_animated_1d
from plot_velocity_animated_window import plot_velocity_animated_window
from plot_velocity_quiver import plot_velocity_quiver
from plot_velocity_quiver_animated import plot_velocity_quiver_animated
from plot_velocity_window import plot_velocity_window
from plot_velocity_x import plot_velocity_x
from plot_velocity_x_animated import plot_velocity_x_animated
from plot_velocity_x_animated_1d import plot_velocity_x_animated_1d
from plot_velocity_x_window import plot_velocity_x_window
from plot_velocity_y import plot_velocity_y
from plot_velocity_y_animated import plot_velocity_y_animated
from plot_velocity_y_animated_1d import plot_velocity_y_animated_1d
from plot_velocity_y_window import plot_velocity_y_window
from plot_velocity_z import plot_velocity_z
from plot_velocity_z_animated import plot_velocity_z_animated
from plot_velocity_z_animated_1d import plot_velocity_z_animated_1d
from plot_velocity_z_window import plot_velocity_z_window

from plot_profile import plot_profile
from plot_profile_animated import plot_profile_animated
from plot_profile_animated_window import plot_profile_animated_window
from plot_profile_window import plot_profile_window
from write_B_to_file import write_B_to_file
from write_density_to_file import write_density_to_file
from write_velocity_to_file import write_velocity_to_file

w_dir='../../output/'
#w_dir='../../output_2_winds_MWR1_1_4_4/'
#w_dir='../../output_snr_rel_M0.1_MWR4_4/'
UNIT_DENSITY=1.672E-24;
UNIT_LENGTH=3.086E17;
UNIT_VELOCITY=2.998E10;
datatype = 'dbl'
ntot = 99

plt.rcParams['image.cmap'] = 'jet'

######### B
plot_B(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_B_spher(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_B_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, 0.1E19, 0.7E19, -0.3E19, 0.3E19, datatype)
#plot_B_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_B_animated_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, 0.1E19, 0.7E19, -0.3E19, 0.3E19, datatype)

#plot_B_quiver(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_B_quiver_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)

#plot_Bx(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_Bx_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, -1E16, 1E16, -1E16, 1E16, datatype)
#plot_By(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_By_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, -1E16, 1E16, -1E16, 1E16, datatype)
#plot_Bz(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_Bz_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, -1E16, 1E16, -1E16, 1E16, datatype)

#plot_B_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_B_1d_series(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_B_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)

########### density

#plot_density(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_density_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, 0.1E19, 0.7E19, -0.3E19, 0.3E19, datatype)
#plot_density_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_density_animated_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, 0.1E19, 0.7E19, -0.3E19, 0.3E19, datatype)

plot_density_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
plot_density_1d_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, 0, 4E17, datatype)
#plot_density_1d_series(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_density_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)

######## pressure

#plot_pressure(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_pressure_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, 0.1E19, 0.7E19, -0.3E19, 0.3E19, datatype)
#plot_pressure_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_pressure_animated_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, 0.1E19, 0.7E19, -0.3E19, 0.3E19, datatype)

#plot_pressure_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_pressure_1d_series(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_pressure_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)

####### temperature

#plot_temperature(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_temperature_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, 0.1E19, 0.7E19, -0.3E19, 0.3E19, datatype)
#plot_temperature_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_temperature_animated_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, 0.1E19, 0.7E19, -0.3E19, 0.3E19, datatype)

#plot_temperature_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_temperature_1d_series(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_temperature_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)

########### gamma

#plot_gamma(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_gamma_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, 0.1E19, 0.7E19, -0.3E19, 0.3E19, datatype)
#plot_gamma_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_gamma_animated_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, 0.1E19, 0.7E19, -0.3E19, 0.3E19, datatype)

#plot_gamma_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_gamma_1d_series(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_gamma_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)

#plot_gamma_rtheta(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_gamma_rtheta_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)


######### velocity

#plot_velocity(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_velocity_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, 0.1E19, 0.7E19, -0.3E19, 0.3E19, datatype)
#plot_velocity_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_velocity_animated_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, 0.1E19, 0.7E19, -0.3E19, 0.3E19, datatype)

#plot_velocity_quiver(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_velocity_quiver_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)

#plot_velocity_x(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_velocity_x_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, -1E16, 1E16, -1E16, 1E16, datatype)
#plot_velocity_y(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_velocity_y_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, -1E16, 1E16, -1E16, 1E16, datatype)
#plot_velocity_z(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_velocity_z_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, -1E16, 1E16, -1E16, 1E16, datatype)

#plot_velocity_x_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_velocity_y_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_velocity_z_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)

#plot_velocity_x_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_velocity_y_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_velocity_z_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)

#plot_velocity_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
plot_velocity_1d_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, 0, 4E17, datatype)
#plot_velocity_1d_series(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_velocity_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)

######### profile

#plot_profile(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_profile_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, -1E17, 1E17, datatype)
#plot_profile_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_profile_animated_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, -1E17, 1E17, datatype)

####### some

#plot_distribution(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_distribution_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_escaped_distribution(150, 2500, w_dir, datatype)
#plot_shock_wave(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_energy(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)


######### particles

#plot_particle_trajectory(ntot, 0, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_particles(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_particles_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
#plot_particles_animated_cyl(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, -100, 100, datatype)
#plot_particles_animated_spher(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, -2E16, 2E16, datatype)

######## writedata
### 1 because change to concentration
write_density_to_file(ntot, w_dir, 1, UNIT_LENGTH, UNIT_VELOCITY, datatype)
write_B_to_file(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)
write_velocity_to_file(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype)

