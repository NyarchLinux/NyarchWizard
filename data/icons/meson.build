application_id = 'moe.nyarchlinux.wizard'

scalable_dir = join_paths('hicolor', 'scalable', 'apps')
install_data(
  join_paths(scalable_dir, ('@0@.svg').format(application_id)),
  install_dir: join_paths(get_option('datadir'), 'icons', scalable_dir)
)

symbolic_dir = join_paths('hicolor', 'symbolic', 'apps')
install_data(
  join_paths(symbolic_dir, ('@0@-symbolic.svg').format(application_id)),
  install_dir: join_paths(get_option('datadir'), 'icons', symbolic_dir)
)
symbolic_dir = join_paths(get_option('datadir'), 'icons/hicolor/symbolic/apps')
install_data (
    'custom-icons/right-large-symbolic.svg',
    install_dir: symbolic_dir
)
install_data (
    'custom-icons/left-large-symbolic.svg',
    install_dir: symbolic_dir
)
install_data (
    'custom-icons/gaming.svg',
    install_dir: symbolic_dir
)
