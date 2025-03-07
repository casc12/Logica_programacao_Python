{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPDRwUiWQadXpmvlz1kyMJG",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/casc12/Logica_programacao_Python/blob/Curso_Programacao/Lista_compras.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_JD2gfW5aKJr",
        "outputId": "33d8e5a7-d1ba-41c1-e3f6-fa67a066467f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o item da lista12\n",
            "Deseja continuar - s para sim ou  n para nãos\n",
            "Digite o item da lista2\n",
            "Deseja continuar - s para sim ou  n para nãos\n",
            "Digite o item da listatrue\n",
            "Deseja continuar - s para sim ou  n para nãon\n",
            "['12', '2', 'true']\n"
          ]
        }
      ],
      "source": [
        "compras = []\n",
        "resp= 's'\n",
        "while resp == \"s\":\n",
        "  compras.append(input(\"Digite o item da lista\"))\n",
        "  resp = input('Deseja continuar - s para sim ou  n para não')\n",
        "#e\n",
        "print(compras)\n"
      ]
    }
  ]
}