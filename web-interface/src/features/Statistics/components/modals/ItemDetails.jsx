import { Modal, ModalOverlay, ModalContent, ModalHeader, ModalCloseButton, ModalBody, Divider, Text } from '@chakra-ui/react';

import { useItemDetailsContext } from '../../hooks';
import { listObjectProperties } from '../../../../utils';

export default function ItemDetails() {

     const itemDeatilsContext = useItemDetailsContext();

     const objectPropertiesList = listObjectProperties(itemDeatilsContext.content);

     const onClose = () => {
          itemDeatilsContext.setIsOpen(false);
          itemDeatilsContext.setTitle("");
          itemDeatilsContext.setDetailsPath("");
     }

     return (
          <Modal isOpen={itemDeatilsContext.isOpen} onClose={onClose}>
               <ModalOverlay />
               <ModalContent>
                    <ModalHeader>{itemDeatilsContext.title}</ModalHeader>
                    <ModalCloseButton />
                    <ModalBody>
                         <Divider borderWidth="2px" borderColor="blue.500" mb={5} />
                         <Text>
                              {objectPropertiesList.map((item) => (
                                   <span key={item.key}
                                        style={{ display: 'block', marginBottom: '8px' }}>
                                        <strong>{item.key}</strong>: {item.value}
                                   </span>
                              ))}
                         </Text>
                    </ModalBody>
               </ModalContent>
          </Modal>
     );
}