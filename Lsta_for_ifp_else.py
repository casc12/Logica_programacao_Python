{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOoRvq0DEcM5zZvQaPWaqZV",
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
        "<a href=\"https://colab.research.google.com/github/casc12/Logica_programacao_Python/blob/Curso_Programacao/Lsta_for_ifp_else.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_JD2gfW5aKJr",
        "outputId": "010f7890-c5d2-4cc6-f868-97d2edbf2ad2"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o item da lista12\n",
            "Deseja continuar - s para sim ou  n para nãos\n",
            "Digite o item da listabanana\n",
            "Deseja continuar - s para sim ou  n para nãos\n",
            "Digite o item da listatrue\n",
            "Deseja continuar - s para sim ou  n para nãon\n",
            "Não encontrei a Banana!!!\n",
            "Encontrei a Banana!!!\n",
            "Não encontrei a Banana!!!\n"
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
        "  if x == \"banana\":\n",
        "    print(\"Encontrei a Banana!!!\")\n",
        "  else:\n",
        "    print('Não encontrei a Banana!!!')\n",
        "  #print(x)\n",
        "#print(compras)\n"
      ]
    }
  ]
}