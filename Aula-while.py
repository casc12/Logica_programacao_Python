{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPqLNClLLrB8w/mFwwvCMFT",
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
        "<a href=\"https://colab.research.google.com/github/casc12/Logica_programacao_Python/blob/Curso_Programacao/Aula-while.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_JD2gfW5aKJr",
        "outputId": "95e83dca-0b6d-498a-8e05-29af0b966b1f"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Digite sua idade 28\n",
            "A idade é maior que 18 é menor que 30\n",
            "Digite nova idade: 3\n"
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
        "while idade > 18:\n",
        "    if idade > 18 and idade < 30:\n",
        "        print(\"A idade é maior que 18 é menor que 30\")\n",
        "        idade = int(input(\"Digite nova idade: \"))\n",
        "    #else:\n",
        "      #print(\"A idade é menor que 18\")\n",
        "\n",
        "\n",
        "#d"
      ]
    }
  ]
}