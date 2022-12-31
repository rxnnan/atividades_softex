const express = require('express');

const server = express();

server.use(express.json()); 

const itens = ['Item 1', 'Item 2', 'Item 3', 'Item 4'];

server.use((req, res, next) => { 
  console.time('Request'); 
  console.log(`Método: ${req.method}; URL: ${req.url}; `);

  next();

  console.log('Finalizou');

  console.timeEnd('Request'); 
});

function checkItemExists(req, res, next) {
  if (!req.body.name) {
    return res.status(400).json({ error: 'item name is required' });
  }
  return next(); 
} 
  
function checkItemInArray(req, res, next) {
  const item = itens[req.params.index];
  if (!item) {
    return res.status(400).json({ error: 'item does not exists' });
  } 

  req.item = item;

  return next();
}

server.get('/itens', (req, res) => {
  return res.json(itens);
}) 

server.get('/itens/:index', checkItemInArray, (req, res) => {
  return res.json(req.item);
})

server.post('/itens', checkItemExists, (req, res) => {
  const { name } = req.body;  
  itens.push(name);
  return res.json(itens); 
})

server.put('/itens/:index', checkItemInArray, checkItemExists, (req, res) => {
  const { index } = req.params; 
  const { name } = req.body;
  itens[index] = name; 
  return res.json(itens);
}); 

server.delete('/itens/:index', checkItemInArray, (req, res) => {
  const { index } = req.params; 

  itens.splice(index, 1); 

  return res.send();
}); 


server.listen(3000);