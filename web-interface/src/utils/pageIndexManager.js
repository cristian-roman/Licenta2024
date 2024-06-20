export function validateIndex(index, pages) {
     index = parseInt(index);
     if (isNaN(index) || index < 1 || index > pages) {
          return ""
     }
     return index;
}

export const getPrevIndex = (current_index, pages_count) => {
     if (current_index === 1) {
          return pages_count;
     }
     return current_index - 1;
}

export const getNextIndex = (current_index, pages_count) => {
     if (current_index === pages_count) {
          return 1;
     }
     return current_index + 1;
}