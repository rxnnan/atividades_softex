import express from 'express';

var app = express();

app.listen(1337);

app.get('/',(request,response)=>{
    return response.send('TESTE DO GET');
});

app.get('/teste',(request,response)=>{
    return response.send('TESTE DO GET EM /teste');
});

app.post('/', function (req, res) {
    return res.send('TESTE DO POST');
  });

app.put('/teste', function (req, res) {
    res.send('TESTE DO PUT EM /teste');
  });

app.delete('/teste', function (req, res) {
    res.send('TESTE DO DELETE EM /teste');
  });