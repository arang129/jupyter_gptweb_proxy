import setuptools

setuptools.setup(
    name="jupyter-gptweb-proxy",
    version='0.0.31',
    url="https://gitlab.mpcdf.mpg.de/khr/jupyter-streamlit-proxy",
    author="Klaus Reuter",
    description="klaus.reuter@mpcdf.mpg.de",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'gptweb = jupyter_gptweb_proxy:setup_gptweb_proxy',
        ]
    },
    package_data={
        'jupyter_gptweb_proxy': ['icons/*'],
    },
)
