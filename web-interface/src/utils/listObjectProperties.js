export default function listObjectProperties(obj) {
     const result = []
     for (const [key, value] of Object.entries(obj)) {
          result.push({
               key: key,
               value: value
          })
     }

     return result;
}