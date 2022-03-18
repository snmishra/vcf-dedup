from distutils.core import setup
from setuptools import find_packages

setup(
    name='vcf-dedup',
    version='0.5.0',
    description='Removal of duplicated variants from a VCF',
    packages=find_packages(),
    scripts=['scripts/vcf_dedupper'],
    url='https://github.com/snmishra/vcf-dedup',
    license='Apache',
    author='Pablo Riesgo Ferreiro',
    author_email='satya.devel@gmail.com',
    requires=['PyVCF3'],
    install_requires=['PyVCF3==1.0.3'],
    keywords=['VCF']
)
