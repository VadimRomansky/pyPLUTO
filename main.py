from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from plot_B_3d_slice2d import plot_B_3d_slice2d
from plot_B_animated_3d_slice2d import plot_B_animated_3d_slice2d
from plot_Bx_3d_slice2d import plot_Bx_3d_slice2d
from plot_Bx_3d_slice2d_window import plot_Bx_3d_slice2d_window
from plot_By_3d_slice2d import plot_By_3d_slice2d
from plot_By_3d_slice2d_window import plot_By_3d_slice2d_window
from plot_Bz_3d_slice2d import plot_Bz_3d_slice2d
from plot_Bz_3d_slice2d_window import plot_Bz_3d_slice2d_window
from plot_density_3d_slice1d import plot_density_3d_slice1d
from plot_density_3d_slice1d_window import plot_density_3d_slice1d_window
from plot_density_animated_3d_slice1d import plot_density_animated_3d_slice1d
from plot_density_1d import plot_density_1d
from plot_density_1d_series import plot_density_1d_series
from plot_distribution import plot_distribution
from plot_escaped_distribution import plot_escaped_distribution
from plot_field_2d import plot_field_2d
from plot_Bx_2d import plot_Bx_2d
from plot_By_2d import plot_By_2d
from plot_Bz_2d import plot_Bz_2d
from plot_gamma_2d import plot_gamma_2d
from plot_particles import plot_particles
from plot_particle_trajectory import plot_particle_trajectory
from plot_particles_animated import plot_particles_animated
from plot_particles_animated_cyl import plot_particles_animated_cyl
from plot_pressure_3d_slice1d import plot_pressure_3d_slice1d
from plot_pressure_3d_slice1d_window import plot_pressure_3d_slice1d_window
from plot_profile_3d_slice1d import plot_profile_3d_slice1d
from plot_profile_3d_slice1d_window import plot_profile_3d_slice1d_window
from plot_profile_animated_3d_slice1d import plot_profile_animated_3d_slice1d
from plot_profile_animated_3d_slice1d_window import plot_profile_animated_3d_slice1d_window
from plot_velocity_animated_2d import plot_velocity_animated_2d
from plot_velocity_animated_1d import plot_velocity_animated_1d
from plot_velocity_animated_3d_slice1d import plot_velocity_animated_3d_slice1d
from plot_velocity_animated_3d_slice2d import plot_velocity_animated_3d_slice2d
from plot_velocity_animated_3d_slice2d_window import plot_velocity_animated_3d_slice2d_window
from plot_velocity_x_3d_slice1d import plot_velocity_x_3d_slice1d
from plot_velocity_x_3d_slice1d_window import plot_velocity_x_3d_slice1d_window
from plot_velocity_x_animated_2d import plot_velocity_x_animated_2d
from plot_pressure_animated import plot_pressure_animated_2d
from plot_density_animated_2d import plot_density_animated_2d
from plot_density_animated_3d_slice2d import plot_density_animated_3d_slice2d
from plot_density_animated_3d_slice2d_window import plot_density_animated_3d_slice2d_window
from plot_density_3d_slice2d import plot_density_3d_slice2d
from plot_density_3d_slice2d_window import plot_density_3d_slice2d_window
from plot_velocity_3d_slice2d import plot_velocity_3d_slice2d
from plot_velocity_3d_slice2d_window import plot_velocity_3d_slice2d_window
from plot_density_animated_1d import plot_density_animated_1d
from plot_density_2d_average1d import plot_density_2d_average1d
from plot_temperature_animated_2d import plot_temperature_animated_2d
from plot_velocity_2d import plot_velocity_2d

w_dir='../../output/'
#w_dir='../../output_2_winds_MWR1_1_4_4/'
#w_dir='../../output_snr_rel_M0.1_MWR4_4/'
UNIT_DENSITY=1.6E-24;
UNIT_LENGTH=3.086E17;
UNIT_VELOCITY=3E10;
ntot = 40

plot_density_1d_series(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)

#plot_Bx_3d_slice2d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_Bx_3d_slice2d_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, -5E14, 5E14, -5E14, 5E14)
#plot_By_3d_slice2d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_By_3d_slice2d_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, -5E14, 5E14, -5E14, 5E14)
#plot_Bz_3d_slice2d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_Bz_3d_slice2d_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, -5E14, 5E14, -5E14, 5E14)
#plot_B_3d_slice2d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)

#plot_field_2d(150, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_gamma_2d(2, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_velocity_2d(6, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_distribution(11, w_dir)
#plot_escaped_distribution(150, 2500, w_dir)
#plot_particles(100, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_density_3d_slice2d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_density_3d_slice1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_density_3d_slice1d_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_pressure_3d_slice1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_pressure_3d_slice1d_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_density_3d_slice2d_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, -5E14, 5E14, -5E14, 5E14)
#plot_velocity_3d_slice2d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_velocity_x_3d_slice1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_profile_3d_slice1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_velocity_x_3d_slice1d_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_profile_3d_slice1d_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_velocity_3d_slice2d_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, -5E14, 5E14, -5E14, 5E14)

#plot_profile_animated_3d_slice1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_profile_animated_3d_slice1d_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)

#plot_B_animated_3d_slice2d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)

#plot_particles_animated(300, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_particles_animated_cyl(300, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, -100, 100)
#plot_velocity_animated_2d(10, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_velocity_animated_1d(100, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_velocity_animated_3d_slice1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_velocity_animated_3d_slice2d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_velocity_animated_3d_slice2d_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, -5E14, 5E14, -5E14, 5E14)
#plot_velocity_x_animated_2d(10, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_pressure_animated_2d(10, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_density_animated_2d(100, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_density_animated_3d_slice2d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_density_animated_3d_slice2d_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, -5E14, 5E14, -5E14, 5E14)
#plot_density_animated_1d(10, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_density_animated_3d_slice1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_density_2d_average1d(100, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_temperature_animated_2d(10, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_particle_trajectory(100, 0, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY)
#plot_smilei_animated(33,'../../output/Fields0.h5','Ex',0,10240,0,200)
