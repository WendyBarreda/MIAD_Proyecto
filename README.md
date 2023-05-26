# <img src="Images/logo.jpg" alt="Logo" width="40" height="35"> Caracterización de adiciones para procesos de contratación publica en infraestructura

<!-- TABLE OF CONTENTS -->
## Tabla de Contenido :octocat:
<details>
  <ol>
    <li>
      <a href="#acerca-del-proyecto-bookmark_tabs">Acerca del proyecto</a>
      <ul>
        <li><a href="#construido-con-hammer_and_wrench">Construido con</a></li>
      </ul>
    </li>
    <li>
      <a href="#configuración-wrench">Configuración</a>
      <ul>
        <li><a href="#prerequisitos-key">Prerequisitos</a></li>
        <li><a href="#instalación-computer">Instalación</a></li>
      </ul>
    </li>
    <li><a href="#modo-de-uso-bulb">Modo de Uso</a></li>
    <li><a href="#desarrolladores-man_technologist-woman_technologist">Desarrolladores</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Acerca del proyecto :bookmark_tabs:

Se analizaron datos de los Procesos de Compra pública registrados en el SECOP I desde su implementación, información del proceso, fase de selección y la adjudicación. La información presentada corresponde a la categoría de datos de Estructuras y edificios permanentes del bien o servicio definido en el proceso de compra de acuerdo a sus características principales.
La finalidad de este proyecto es construir una API que permite estimar la probabilidad que un nuevo contrato presente adiciones. 

Puedes acceder a la API en el siguiente [enlace](https://lookerstudio.google.com/u/0/reporting/09c4c9c1-7389-4096-97a2-969ba6a47a55/page/p_77uk5sr35c)

<p align="right">(<a href="#tabla-de-contenido-octocat">back to top</a>)</p>

## Construido con :hammer_and_wrench:

* [![Python][Python]][Python-url]
* [![Flask][Flask]][Flask-url]
* [![scikit-learn][scikit-learn]][scikit-learn-url]

<p align="right">(<a href="#tabla-de-contenido-octocat">back to top</a>)</p>

<!-- GETTING STARTED -->
## Configuración :wrench:

Se necesita un ambiente python
* Pyhton 3 o superior

<p align="right">(<a href="#tabla-de-contenido-octocat">back to top</a>)</p>

### Prerequisitos :key:
* Scikit-learn

```sh
  pip install scikit-learn
  ```
* Flask

```sh
  pip install Flask
  ```

<p align="right">(<a href="#tabla-de-contenido-octocat">back to top</a>)</p>

### Instalación :computer:

1. Clona el repositorio
   ```sh
   git clone https://github.com/WendyBarreda/MIAD_Proyecto.git
   ```
2. Abre tu consola de pyhton y situate en la carpeta de la API
   ```sh
   cd /MIAD_Proyecto/API
   ```
3. Ejecuta el siguiente comando
   ```py
   python3 api.py
   ```

<p align="right">(<a href="#tabla-de-contenido-octocat">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Modo de uso :bulb:

_Por favor dirigete al siguiente documento_

<p><a href="https://github.com/WendyBarreda/MIAD_Proyecto/blob/main/manual.pdf">Manual</a>.</p>

<p align="right">(<a href="#tabla-de-contenido-octocat">back to top</a>)</p>

<!-- CONTACT -->
## Desarrolladores :man_technologist: :woman_technologist:
* Harold Rodríguez
* Jose Rivera
* Wendy Barred

<p align="right">(<a href="#tabla-de-contenido-octocat">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/2.3.x/
[scikit-learn]: https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white
[scikit-learn-url]: https://scikit-learn.org/stable/


