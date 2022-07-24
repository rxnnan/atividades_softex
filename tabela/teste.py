import pandas as pd
df = pd.read_csv("notas_alunos.csv", sep=";")
df["média:"] = (df["nota_1:"]+df["nota_2:"]) / 2
df.loc[df["média:"] >= 7, "situação"] = "APROVADO"
df.loc[df["média:"] < 7, "situação"] = "REPROVADO"
df.loc[df["faltas:"] > 5, "situação"] = "REPROVADO"
df.to_csv("alunos_situacao.csv", sep=";")
print(df)
print("-"*53)
print("O maior número de faltas foi: "+str(df["faltas:"].max()))
print("A média geral das notas dos alunos foi: "+str(df["média:"].median()))
print("A maior média foi: "+str(df["média:"].max()))
