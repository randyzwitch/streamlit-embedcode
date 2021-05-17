import setuptools

setuptools.setup(
    name="streamlit-embedcode",
    version="0.1.2",
    author="Randy Zwitch",
    author_email="randy@streamlit.io",
    description="Streamlit component for embedded code snippets",
    long_description="Streamlit component for embedded code snippets",
    long_description_content_type="text/plain",
    url="https://github.com/randyzwitch/streamlit-embedcode",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=["streamlit >= 0.63"],
)
