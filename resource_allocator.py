import logging
from typing import Dict, Optional

logger = logging.getLogger(__name__)

class ResourceAllocator:
    """
    Manages resource allocation across the ecosystem. 
    Optimizes resource distribution to maximize revenue generation.
    """

    def __init__(self):
        self.resources = {}
        self.current_allocations = {}

    def allocate_resource(self, resource_id: str, amount: float) -> bool:
        """
        Allocates a specified amount of a resource.
        
        Args:
            resource_id: Unique identifier for the resource
            amount: Amount to allocate
            
        Returns:
            True if allocation was successful, False otherwise
        """
        try:
            if resource_id in self.resources:
                self.current_allocations[resource_id] = amount
                logger.info(f"Allocated {amount} of resource {resource_id}")
                return True
            else:
                logger.error(f"Resource {resource_id} does not exist")
                raise ValueError("Invalid resource ID")

        except Exception as e:
            logger.error(f"Allocation failed for resource {resource_id}: {str(e)}")
            return False

    def release_resource(self, resource_id: str) -> bool:
        """
        Releases a previously allocated resource.
        
        Args:
            resource_id: Unique identifier for the resource
            
        Returns:
            True if release was successful, False otherwise
        """
        try:
            if resource_id in self.current_allocations:
                del self.current_allocations[resource_id]
                logger.info(f"Released resource {resource_id}")
                return True
            else:
                logger.error(f"Resource {resource_id} not allocated")
                raise ValueError("Resource not allocated")

        except Exception as e:
            logger.error(f"Release failed for resource {resource_id}: {str(e)}")
            return False

    def get_available_resources(self) -> Dict[str, float]:
        """
        Returns a dictionary of available resources and their quantities.
        
        Returns:
            Dictionary of resource IDs to available amounts
        """
        try:
            return self.resources.copy()
        except Exception as e:
            logger.error(f"Failed to retrieve available resources: {str(e)}")
            raise

    def check_resource_availability(self, resource_id: str) -> Optional[float]:
        """
        Checks if a specific resource is available for allocation.
        
        Args:
            resource_id: Unique identifier for the resource
            
        Returns:
            Available amount of the resource or None if unavailable
        """
        try:
            return self.resources.get(resource_id)
        except Exception as e:
            logger.error(f"Failed to check resource availability: {str(e)}")
            raise