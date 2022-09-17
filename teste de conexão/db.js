import Sequelize from 'sequelize'

const sequelize = new Sequelize('sistemadeteste', 'root', 'rennan123', {
    host: "localhost",
    dialect: 'mysql'
})

sequelize.authenticate().then(function(){
    console.log("Conexão realizada com sucesso!")
}).catch(function(erro){
    console.log("Falha na conexão: "+erro)
})
 