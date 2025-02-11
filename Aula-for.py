{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNGSH9Qxon1WloOTf75rBcX",
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
        "<a href=\"https://colab.research.google.com/github/casc12/Logica_programacao_Python/blob/Curso_Programacao/Aula-for.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_JD2gfW5aKJr",
        "outputId": "9bc637ff-6b11-4055-fb0f-8ada3ad217c5"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Digite sua idade 28\n",
            "A idade é maior que 18 é menor que 30\n",
            "Digite nova idade: 13\n"
          ]
        }
      ],
      "source": [
        "\"\"\"nome = \"\"\n",
        "nome = input(\"Digite seu nome\")\n",
        "print(nome)\n",
        "print(5*5) \"\"\"\n",
        "idade = int(input(\"Digite sua idade \"))\n",
        "# print(idade)\n",
        "\n",
        "\"\"\"\"\"while idade > 18:\n",
        "    if idade > 18 and idade < 30:\n",
        "        print(\"A idade é maior que 18 é menor que 30\")\n",
        "        idade = int(input(\"Digite nova idade: \"))\n",
        "    #else:\n",
        "      #print(\"A idade é menor que 18\")\"\"\"\n",
        "\n",
        "x = 1\n",
        "for x in range(3):\n",
        "  if idade > 18 and idade < 30:\n",
        "        print(\"A idade é maior que 18 é menor que 30\")\n",
        "        idade = int(input(\"Digite nova idade: \"))\n",
        " #d"
      ]
    }
  ]
}