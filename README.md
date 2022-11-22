# ticketManagement
For successfully completing this task create a rudimentary event ticket managementsolution. The overall goal is to be able to create events and manage the number of peopleaccessing each event.



Requisitos
• A aplicação deve ter uma página web para criar eventos. Cada evento deve ter umNome, Data e número inicial de ingressos.

• Assuma que este aplicativo terá apenas um usuário (portanto, não há necessidade de implementar autenticação).

• Na página do evento, o usuário deve ser capaz de ver o número total de ingressos e quantos foram resgatados. A página também deve conter um botão para atualizar os contadores.

• Cada ingresso pode ser representado por um token único. • O usuário deve poder adicionar mais ingressos a um evento.

• O aplicativo deve ter uma página onde o usuário possa verificar o status de um ticket. Um bilhete pode ser resgatado ou ok.

• O aplicativo deve expor um endpoint para resgatar um ticket:





from ticket.config import *
from ticket.model import *
db_conn = DBConnectionHandler()
engine = db_conn.get_engine()
Base.metadata.create_all(engine)