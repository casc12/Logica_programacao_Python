{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOVRGhXai1/e76bGJA5VBr3",
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
        "<a href=\"https://colab.research.google.com/github/casc12/Logica_programacao_Python/blob/Curso_Programacao/Lista_compras_for.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_JD2gfW5aKJr",
        "outputId": "92dc29c8-ce68-4df1-8145-c7769ffb6d3b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o item da lista12\n",
            "Deseja continuar - s para sim ou  n para nãos\n",
            "Digite o item da listatrue\n",
            "Deseja continuar - s para sim ou  n para nãon\n",
            "12\n",
            "true\n"
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
        "for x in compras:\n",
        "  print(x)\n",
        "#print(compras)\n"
      ]
    }
  ]
}